from flask import Blueprint, jsonify, request
from src.service.categories import Category_service
from flask import make_response
from flask_jwt_extended import jwt_required


category_bp = Blueprint('category_bp', __name__, url_prefix='/category')

service = Category_service()


@category_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_users():
    user_id = request.args.get('user_id')
    data, status_code = service.get_all(user_id)
    response = make_response(data, status_code)
    return response, status_code


@category_bp.route('', methods=['POST'])
@jwt_required()
def create():
    data = request.get_json()
    user, status_code = service.create(data)
    return user, status_code


@category_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_id(id):
    data, status_code = service.get_by_id(id)
    response = make_response(data, status_code)
    return response, status_code


@category_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def edit_category(id):
    data = request.get_json()
    response = service.edit_category(id, data)
    return response


@category_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    response = service.delete_category(id)
    return response
