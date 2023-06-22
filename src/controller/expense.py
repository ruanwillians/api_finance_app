from flask import Blueprint, jsonify, request
from src.service.expense import expenseService
from flask import make_response
from flask_jwt_extended import jwt_required


expense_bp = Blueprint('expense_bp', __name__, url_prefix='/expense')

service = expenseService()


@expense_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_expenses():
    user_id = request.args.get('user_id')
    category_id = request.args.get('category_id')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    data, status_code = service.get_all(
        user_id, category_id, start_date, end_date)
    response = make_response(data, status_code)
    return response, status_code


@expense_bp.route('', methods=['POST'])
@jwt_required()
def create():
    data = request.get_json()
    response, status_code = service.create(data)
    return data, status_code


@expense_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_id(id):
    data, status_code = service.get_by_id(id)
    response = make_response(data, status_code)
    return response, status_code


@expense_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def edit_expense(id):
    data = request.get_json()
    response = service.edit_expense(id, data)
    return response


@expense_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    response = service.delete_expense(id)
    return response
