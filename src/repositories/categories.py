from database import db
from src.model.categories import Categories
from database import db
from uuid import uuid4
from src.schema.categories import Category_schema

category_schema = Category_schema(many=True)


class Category_repository():

    def save(self, data):
        db.session.add(data)
        db.session.commit()

    def generate_item(seld, data):
        name = data['name']
        description = data['description']
        user_id = data['user_id']

        item = Categories(name=name,
                          description=description, user_id=user_id)

        return item

    def get_all(self, user_id):
        if user_id:
            data = Categories.query.filter_by(user_id=user_id).all()
            serialized_data = category_schema.dump(data)
            return serialized_data
        else:
            data = Categories.query.all()
            serialized_data = category_schema.dump(data)
            return serialized_data

    def get_by_id(self, id):
        data = Categories.query.filter_by(id=id).first()
        if not data:
            return {'error': 'Category not found'}
        else:
            serialized_data = Categories.json(data)
            return serialized_data

    def create(self, data):
        item = self.generate_item(data)
        self.save(item)
        serialized_data = category_schema.dump([item])
        return serialized_data

    def edit_category(self, id, data):
        category = Categories.query.filter_by(id=id).first()
        if not category:
            return {'error': 'User not found'}
        else:
            if 'description' in data:
                category.description = data['description']
            if 'name' in data:
                category.name = data['name']

            self.save(category)
            serialized_data = Categories.json(category)
            return serialized_data

    def delete_category(self, id):
        category = Categories.query.filter_by(id=id).first()

        if not category:
            return {'error': 'category not found'}

        db.session.delete(category)
        db.session.commit()

        return {'message': 'category deleted successfully'}
