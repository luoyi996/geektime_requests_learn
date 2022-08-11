import pytest

from geektime_requests_learn.homework.api.login import Login
from geektime_requests_learn.homework.model.data_stream.login_params import LoginParams


class TestLiteMallUserLogin:
    def setup_class(self):
        self.user = Login()

    @pytest.mark.parametrize('params', [
        {"username": 'test123', "password": 'test123'}
    ])
    def test_login_success(self, params):
        """
        登录成功：验证接口是否正确
        :param params: LoginParams 对象
        :return: None
        """
        param = LoginParams(**params)
        r = self.user.user_login(param)
        assert r.json()['errno'] == 0
        assert r.json()['data']['userInfo']['nickName'] == param.username
        assert r.json()["errmsg"] == "成功"

    @pytest.mark.parametrize('params', [
        {"username": 'test123', "password": 'test001'},
        {"username": 'test123', "password": '1sdsda'},
        {"username": 'test123', "password": ''},
        {"username": 'test123', "password": '....'},
        {"username": 'test123', "password": 111},
        {"username": 'test123', "password": '!%^&'},
        {"username": 'test123', "password": '    '},
    ])
    def test_login_password_fail(self, params):
        """
        前置条件：正确的账号
        密码输入框测试
        :param params:
        :return:
        """
        param = LoginParams(**params)
        r = self.user.user_login(param)
        assert r.status_code == 200
        assert r.json()['errno'] == 700
        assert r.json()['errmsg'] == '账号密码不对'

    @pytest.mark.parametrize('params', [
        {"username": '', "password": 'test123'},
        {"username": '1asde', "password": 'test123'},
        {"username": '!@#%^', "password": 'test123'},
        {"username": '    ', "password": 'test123'},
        {"username": 1111, "password": "test123"},
    ])
    def test_login_username_fail(self, params):
        """
        前置条件：正确的密码
        账号输入框测试
        :param params:
        :return:
        """
        param = LoginParams(**params)
        r = self.user.user_login(param)
        assert r.status_code == 200
        assert r.json()['errno'] == 700
        assert r.json()['errmsg'] == '账号不存在'

    @pytest.mark.parametrize('params', [
        {"username": 'test123', "password": 'test001'},
        {"username": 'test001', "password": 'test123'},
        {"username": 'test001', "password": 'test001'}
    ])
    def test_login_combination_fail(self, params):
        """
        登录业务错误的账号密码组合测试
        :param params:
        :return:
        """
        param = LoginParams(**params)
        r = self.user.user_login(param)
        assert r.status_code == 200
        assert r.json()['errno'] != 0
        assert r.json()['errmsg'] != '成功'
