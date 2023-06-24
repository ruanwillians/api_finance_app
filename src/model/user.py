from database import db
from sqlalchemy import Column, Integer, String, Float
from werkzeug.security import check_password_hash, generate_password_hash


class Users(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    available = Column(Float, nullable=False)
    balance = Column(Float, nullable=False)

    def __init__(self, name, email, password, balance, available):
        self.name = name
        self.email = email
        self.set_password(password)
        self.balance = balance
        self.available = available

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'balance': self.balance,
            'available': self.available
        }

    def json_token(self, token):
        return {
            'token': token,
            'email:': self.email,
            'id': self.id,
            'name': self.name,
            'available': self.available,
        }
