from flask import Blueprint, jsonify, request
from src.service.user import User_service
from flask import make_response
from flask_jwt_extended import create_access_token, jwt_required


user_bp = Blueprint('user_bp', __name__, url_prefix='/user')

service = User_service()


@user_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_users():
    data, status_code = service.get_all()
    response = make_response(data, status_code)
    return response, status_code


@user_bp.route('', methods=['POST'])
def create():
    data = request.get_json()
    user, status_code = service.create(data)
    return user, status_code


@user_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def getId(id):
    data, status_code = service.get_by_id(id)
    response = make_response(data, status_code)
    return response, status_code


@user_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def edit(id):
    data = request.get_json()
    response = service.edit_user(id, data)
    return response


@user_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    response = service.delete_user(id)
    return response
