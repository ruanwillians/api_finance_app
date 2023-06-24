from database import db
from src.model.movement import Movement
from database import db
from uuid import uuid4
from src.schema.movement import MovementSchema

movement_schema = MovementSchema(many=True)


class Movement_repository():

    def save(self, data):
        db.session.add(data)
        db.session.commit()

    def generate_item(seld, data):
        description = data['description']
        date = data['date']
        value = data['value']
        category_id = data['category_id']
        user_id = data['user_id']
        type = data['type']

        item = Movement(date=date, description=description,
                        value=value, category_id=category_id, type=type, user_id=user_id)

        return item

    def get_all(self, user_id, category_id, start_date, end_date, type):
        query = Movement.query

        if start_date and end_date:
            query = query.filter(Movement.date.between(start_date, end_date))

        if user_id:
            query = query.filter(Movement.user_id == user_id)

        if category_id:
            query = query.filter(Movement.category_id == category_id)

        if type is not None:
            query = query.filter(Movement.type == type)

        data = query.all()

        if not data:
            return {'error': 'Movement not found'}
        else:
            serialized_data = movement_schema.dump(data)
            return serialized_data

    def get_by_id(self, id):
        data = Movement.query.filter_by(id=id).first()
        if not data:
            return {'error': 'Movement not found'}
        else:
            serialized_data = Movement.json(data)
            return serialized_data

    def create(self, data):
        item = self.generate_item(data)
        self.save(item)
        return item

    def edit_movement(self, id, data):
        movement = Movement.query.filter_by(id=id).first()
        if not movement:
            return {'error': 'User not found'}
        else:
            if 'description' in data:
                movement.description = data['description']
            if 'date' in data:
                movement.date = data['date']
            if 'value' in data:
                movement.value = data['value']
            if 'category_id' in data:
                movement.category_id = data['category_id']
            if 'type' in data:
                movement.type = data['type']

            self.save(movement)
            serialized_data = Movement.json(movement)
            return serialized_data

    def delete_movement(self, id):
        movement = Movement.query.filter_by(id=id).first()

        if not movement:
            return {'error': 'movement not found'}

        db.session.delete(movement)
        db.session.commit()

        return {'message': 'movement deleted successfully'}
