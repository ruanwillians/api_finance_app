from src.repositories.user import user_repository

repository = user_repository()


class user_service():

    def get_all(self):
        data = repository.get_all()
        return data, 200

    def login(self, data):
        response = repository.login(data)
        if "error" in response:
            return response["error"], 401
        else:
            return response, 200

    def get_by_id(self, id):
        data = repository.get_by_id(id)
        if "error" in data:
            return data["error"], 404
        else:
            return data, 200

    def create(self, data):
        user = repository.create(data)
        if "error" in data:
            return data["error"], 409
        else:
            return user, 201

    def edit_user(self, id, data):
        user = repository.edit_user(id, data)
        if "error" in data:
            return data["error"], 404
        else:
            return user, 201

    def delete_user(self, id):
        data = repository.delete_user(id)
        if "error" in data:
            return data["error"], 404
        else:
            return data, 201
