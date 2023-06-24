from database import db
from src.model.user import Users
from database import db
from src.schema.user import user_schema

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
        available = data['available']

        item = Users(balance=balance,
                     email=email, password=password, name=name, available=available)

        return item

    def get_all(self):
        data = Users.query.all()
        serialized_data = user_schema.dump(data)
        return serialized_data

    def get_by_id(self, id):
        data = Users.query.filter_by(id=id).first()
        if not data:
            return {'error': 'User not found'}, 404
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
            if 'available' in data:
                user.available = data['available']

            self.save(user)
            serialized_data = Users.json(user)
            return serialized_data

    def delete_user(self, id):
        user = Users.query.filter_by(id=id).first()

        if not user:
            return {'error': 'User not found'}, 404

        db.session.delete(user)
        db.session.commit()

        return {'message': 'User deleted successfully'}
