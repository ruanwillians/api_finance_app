from flask import Blueprint, request
from src.service.login import login_service


login_bp = Blueprint('login_bp', __name__, url_prefix='/login')

service = login_service()


@login_bp.route('', methods=['POST'])
def login():
    data = request.get_json()
    response, status_code = service.login(data)
    return response, status_code
