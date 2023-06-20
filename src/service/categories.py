from src.repositories.categories import category_repository

repository = category_repository()


class category_service():

    def get_all(self, user_id):
        data = repository.get_all(user_id)
        return data, 200

    def get_by_id(self, id):
        data = repository.get_by_id(id)
        if "error" in data:
            return {"error": "User not found"}, 404
        else:
            return data, 200

    def create(self, data):
        user = repository.create(data)
        return user, 201

    def edit_category(self, id, data):
        user = repository.edit_category(id, data)
        if "error" in data:
            return data["error"], 404
        else:
            return user, 201

    def delete_category(self, id):
        data = repository.delete_category(id)
        if "error" in data:
            return data["error"], 404
        else:
            return data, 201
