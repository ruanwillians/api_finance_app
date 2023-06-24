from flask import Blueprint, jsonify, request
from src.service.movement import Movement_service
from flask import make_response
from flask_jwt_extended import jwt_required


movement_bp = Blueprint('movement_bp', __name__, url_prefix='/movement')

service = Movement_service()


@movement_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_movements():
    user_id = request.args.get('user_id')
    category_id = request.args.get('category_id')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    type = request.args.get('type')
    data, status_code = service.get_all(
        user_id, category_id, start_date, end_date, type)
    response = make_response(data, status_code)
    return response, status_code


@movement_bp.route('', methods=['POST'])
@jwt_required()
def create():
    data = request.get_json()
    response, status_code = service.create(data)
    return data, status_code


@movement_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_id(id):
    data, status_code = service.get_by_id(id)
    response = make_response(data, status_code)
    return response, status_code


@movement_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def edit_movement(id):
    data = request.get_json()
    response = service.edit_movement(id, data)
    return response


@movement_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    response = service.delete_movement(id)
    return response
