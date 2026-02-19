import pytest
from test_data.users_data import success_user_data
from helpers.api_client import ApiClient
from api.users.api_user import AuthApi
from utils.config import BASE_URL

@pytest.fixture(scope='session')
def api_client_user_fixture(request):
    client = ApiClient(base_url=BASE_URL)
    return client

@pytest.fixture(scope='function')
def login_user_fixture(api_client_user_fixture, request):
    client = api_client_user_fixture
    auth = AuthApi(client)
    user_data = success_user_data()
    login_resp = auth.register(user_data)

    return login_resp
