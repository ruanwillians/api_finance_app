from src.repositories.expense import expenseRepository

repository = expenseRepository()


class expenseService():

    def get_all(self, user_id, category_id, start_date, end_date):
        data = repository.get_all(user_id, category_id, start_date, end_date)
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
        data = repository.create(data)
        return data, 201

    def edit_expense(self, id, data):
        user = repository.edit_expense(id, data)
        if "error" in data:
            return data["error"], 404
        else:
            return user, 201

    def delete_expense(self, id):
        data = repository.delete_expense(id)
        if "error" in data:
            return data["error"], 404
        else:
            return data, 201
