from database import db
from src.model.user import Users
from database import db
from src.schema.user import user_schema
from flask_jwt_extended import create_access_token
from flask import jsonify
from flask_bcrypt import check_password_hash

user_schema = user_schema(many=True)


class user_repository():

    def save(self, data):
        db.session.add(data)
        db.session.commit()

    def generate_item(seld, data):
        balance = data['balance']
        email = data['email']
        password = data['password']
        name = data['name']

        item = Users(balance=balance,
                     email=email, password=password, name=name)

        return item

    def get_all(self):
        data = Users.query.all()
        serialized_data = user_schema.dump(data)
        return serialized_data

    def login(self, data):
        email = data.get('email')
        password = data.get('password')

        user = Users.query.filter(Users.email == email).first()
        if not user:
            return {'error': 'User not found'}

        if not check_password_hash(user.password, password):
            return {'error': 'Invalid password'}

        access_token = create_access_token(identity=email)
        print(access_token)
        return Users.json_token(access_token)

    def get_by_id(self, id):
        data = Users.query.filter_by(id=id).first()
        if not data:
            return {'error': 'User not found'}
        else:
            serialized_data = Users.json(data)
            return serialized_data

    def create(self, data):
        email = data.get('email')

        user = Users.query.filter_by(email=email).first()
        if user:
            return {'error': 'Email already exists'}

        item = self.generate_item(data)
        self.save(item)
        serialized_data = user_schema.dump([item])
        return serialized_data

    def edit_user(self, id, data):
        user = Users.query.filter_by(id=id).first()
        if not user:
            return {'error': 'User not found'}
        else:
            if 'balance' in data:
                user.balance = data['balance']
            if 'email' in data:
                user.email = data['email']
            if 'name' in data:
                user.name = data['name']

            self.save(user)
            serialized_data = Users.json(user)
            return serialized_data

    def delete_user(self, id):
        user = Users.query.filter_by(id=id).first()

        if not user:
            return {'error': 'User not found'}

        db.session.delete(user)
        db.session.commit()

        return {'message': 'User deleted successfully'}
