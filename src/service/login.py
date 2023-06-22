from src.repositories.login import login_repository

repository = login_repository()


class login_service():

    def login(self, data):
        response = repository.login(data)
        if "error" in response:
            return response["error"], 401
        else:
            return response, 200
