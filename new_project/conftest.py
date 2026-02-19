import pytest
from test_data.users_data import success_user_data
from helpers.api_client import ApiClient
from api.users.api_user import AuthClient
from utils.config import BASE_URL

@pytest.fixture(scope='session')
def api_client_user_fixture(request):
    client = AuthClient(base_url=BASE_URL)
    return client

@pytest.fixture()
def login_user_fixture(api_client_user_fixture, request):
    user_data = success_user_data()
    client = api_client_user_fixture
    login_resp = client._post_api(endpoint="/users/add", data=user_data)
    return login_resp
