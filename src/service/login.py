from src.repositories.login import Login_repository

repository = Login_repository()


class Login_service():

    def login(self, data):
        response = repository.login(data)
        if "error" in response:
            return response["error"], 401
        else:
            return response, 200
