from helpers.global_test_data import get_route_by_entity

from helpers.api_client import ApiClient

class Users:
    """Объект пользователя"""

    def __init__(self, client: ApiClient):
        self.client = client
        self.id = None
        self.resp = None


    def create(self, data: dict):

        self.resp = self.client._post_api()