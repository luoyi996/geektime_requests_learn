import pytest

from geektime_requests_learn.LiteMall.api.test_method import MallLoginMethod
from geektime_requests_learn.LiteMall.utils.get_yaml_data import GetData
from geektime_requests_learn.LiteMall.utils.log import log

data = GetData().load_yaml('data/admin_login_user.yaml')


class TestLogin:
    def setup_class(self):
        log().info(f'{self.setup_class.__name__} 初始化数据')
        self.admin = MallLoginMethod()

    def setup(self):
        ...

    def teardown(self):
        ...

    def teardown_class(self):
        ...

    @pytest.mark.parametrize("username, password, code", data["data_success"])
    def test_admin_login_success(self, username, password, code):
        r = self.admin.login(username, password, code)
        assert r.status_code == 200
        assert r.json()["errmsg"] == "成功"
        assert r.json()["data"]["adminInfo"]["nickName"] == username

    @pytest.mark.parametrize("username, password, code", data["data_fail"])
    def test_admin_login_fail(self, username, password, code):
        r = self.admin.login(username, password, code)
        assert r.status_code == 200
        if r.json()["errno"] == 605:
            assert r.json()["errmsg"] == "用户帐号或密码不正确"
        elif r.json()["errno"] == 401:
            assert r.json()["errmsg"] == "参数不对"
        else:
            log().error(f'未知错误，请求方法：{self.test_admin_login_fail.__name__}的数据为：{username, password, code}')


