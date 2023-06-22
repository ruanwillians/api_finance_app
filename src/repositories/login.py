from src.model.user import Users
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash


class login_repository():

    def login(self, data):
        email = data.get('email')
        password = data.get('password')

        user = Users.query.filter(Users.email == email).first()
        if not user:
            return {'error': 'User not found'}

        if not check_password_hash(user.password, password):
            return {'error': 'Invalid password'}

        access_token = create_access_token(identity=email)
        return Users.json_token(user, access_token)
