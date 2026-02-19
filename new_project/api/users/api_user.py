from helpers.api_client import ApiClient


class AuthApi:
    """Клиент с поддержкой авторизации и токенов"""
    def __init__(self, client: ApiClient):
        self.client = client
        self.token = None
        self.refresh_token = None

    def register(self, user_data):
        """Регистрация нового пользователя"""
        resp = self.client._post_api("/users/add", json=user_data)
        return resp

    def login(self, name, password):
        """Логин и получение токена"""
        data = {
            "username": name,
            "password": password
        }
        resp = self.client._post_api("/auth/login", json=data)
        resp_json = resp.json()
        print(data)
        print(resp_json)
        self.token = resp_json.get("token")
        self.refresh_token = resp_json.get("refreshToken")

        return resp

    def get_info_user(self):
        """Получить информацию о текущем пользователе"""
        resp = self.client._get_api("/auth/me")
        return resp
