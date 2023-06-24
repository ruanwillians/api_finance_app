from datetime import datetime
from database import db
from sqlalchemy import Column, Float, Integer, String, ForeignKey, DateTime
from src.model.categories import Categories
from src.model.user import Users


class Movement(db.Model):
    __tablename__ = 'movement'

    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    description = Column(String)
    date = Column(DateTime, nullable=False, default=datetime.now)
    type = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category = db.relationship('Categories', backref='movement')
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = db.relationship('Users', backref='movement')

    def __init__(self, value, date, description, category_id, user_id, type):
        self.value = value
        self.date = date
        self.description = description
        self.category_id = category_id
        self.user_id = user_id
        self.type = type

    def json(self):
        return {
            "value": self.value,
            "date": self.date,
            "description": self.description,
            "category_id": self.category_id,
            "user_id": self.user_id,
            "type": self.type
        }
