from src.repositories.movement import Movement_repository

repository = Movement_repository()


class Movement_service():

    def get_all(self, user_id, category_id, start_date, end_date, type):
        data = repository.get_all(
            user_id, category_id, start_date, end_date, type)
        if "error" in data:
            return data["error"], 404
        else:
            return data, 200

    def get_by_id(self, id):
        data = repository.get_by_id(id)
        if "error" in data:
            return data["error"], 404
        else:
            return data, 200

    def create(self, data):
        movement = repository.create(data)
        if "error" in movement:
            return movement["error"], 409
        else:
            return movement, 201

    def edit_movement(self, id, data):
        user = repository.edit_movement(id, data)
        if "error" in user:
            return user["error"], 404
        else:
            return user, 201

    def delete_movement(self, id):
        data = repository.delete_movement(id)
        if "error" in data:
            return data["error"], 404
        else:
            return data, 201
