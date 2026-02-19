from checker.check_basic import check_status_code


class TestLoginUser:
    def test_login_user(self, login_user_fixture):
        resp = login_user_fixture
        check_status_code(resp, 201)
