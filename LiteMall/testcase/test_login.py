import pytest

from geektime_requests_learn.LiteMall.api.test_method import MallLoginMethod


class TestLogin:
    def setup_class(self):
        self.admin = MallLoginMethod()

    def setup(self):
        ...

    def teardown(self):
        ...

    def teardown_class(self):
        ...

    @pytest.mark.parametrize("username, password, code", [
        ('admin123', 'admin123', ''),
        ('mall123', 'mall123', ''),
        ('promotion123', 'promotion123', '')
    ])
    def test_admin_login_success(self, username, password, code):
        r = self.admin.login(username, password, code)
        assert r.status_code == 200
        assert r.json()["errmsg"] == "成功"
        assert r.json()["data"]["adminInfo"]["nickName"] == username

    @pytest.mark.parametrize("username, password, code", [
        ('admin123', 'admin123', ''),
        ('mall123', 'mall123', ''),
        ('promotion123', 'promotion123', '')
    ])
    def test_admin_login_fail(self, username, password, code):
        r = self.admin.login(username, password, code)
        assert r.status_code == 200
        assert r.json()["errmsg"] != "成功"
        if r.json()["errno"] == 605:
            ...
        elif r.json()["errno"] == 404:
            ...

