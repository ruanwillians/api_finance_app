from database import db
from sqlalchemy import Column, Integer, String
from flask_bcrypt import check_password_hash, generate_password_hash


class Users(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    balance = Column(Integer, nullable=False)

    def __init__(self, name, email, password, balance):
        self.name = name
        self.email = email
        self.set_password(password)
        self.balance = balance

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'balance': self.balance
        }

    def json_token(token):
        return {
            'token': token
        }
