from helpers.api_client import ApiClient


class AuthClient(ApiClient):
    """Клиент с поддержкой авторизации и токенов"""
    def __init__(self, base_url):
        super().__init__(base_url)
        self.token = None
        self.refresh_token = None

    def register(self, user_data):
        """Регистрация нового пользователя"""
        resp = self._post_api("/users/add", data=user_data)
        return resp

    def login(self, name, password):
        """Логин и получение токена"""
        data = {
            "username": name,
            "password": password
        }
        resp = self._post_api("/auth/login", data=data)
        resp_json = resp.json()
        self.token = resp_json.get("token")
        self.refresh_token = resp_json.get("refreshToken")

        return resp

    def get_info_user(self):
        """Получить информацию о текущем пользователе"""
        resp = self._get_api("/auth/me")
        return resp
