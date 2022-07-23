import requests
from tools.mall import Mall


class TestMall:
    def setup_class(self):
        mall = Mall()
        self.login = mall.login
        self.user_addr = mall.user_addr
        self.first_page = mall.first_page
        self.order_manage = mall.order_manage
        self.update_apple = mall.update_apple
        self.create_banana = mall.create_banana
        self.logout = mall.logout
        print('setup_class method')

    def setup(self):
        print('setup method')

    def test_login(self):
        user = 'admin123'
        passwd = 'admin123'
        code = ''
        r = self.login(username=user, password=passwd, code=code)
        assert r.status_code == 200
        assert r.json()['errmsg'] == '成功'
        assert r.json()['data']['adminInfo']['nickName'] == 'admin123'

    def test_logout(self):
        r = self.logout()
        assert r.status_code == 200
        assert r.json()['errmsg'] == '成功'

    def test_user_addr(self):
        r = self.user_addr()
        assert r.status_code == 200
        assert r.json()['errmsg'] == '成功'

    def test_first_page(self):
        r = self.first_page()
        assert r.status_code == 200
        assert r.json()['errmsg'] == '成功'
        assert "userTotal" in r.json()['data'].keys()

    def test_order_manage(self):
        r = self.order_manage()
        assert r.status_code == 200
        assert r.json()['errmsg'] == '成功'
        assert "orderStatus" in r.json()['data']['list'][0].keys()

    def test_update_apple(self):
        r = self.update_apple()
        assert r.status_code == 200
        assert r.json()['errmsg'] == "成功"

    # def test_create_banana(self):
    #     """测试未添加的商品"""
    #     r = self.create_banana()
    #     assert r.status_code == 200
    #     assert r.json()['errmsg'] == "成功"

    def test_added_banana(self):
        """测试添加的商品"""
        r = self.create_banana()
        if r.json()['errmsg'] == "商品名已经存在":
            # 判断已添加的商品
            assert r.status_code == 200
            assert r.json()['errmsg'] == "商品名已经存在"
        else:
            # 添加商品
            assert r.status_code == 200
            assert r.json()['errmsg'] == "成功"

    def teardown(self):
        print("teardown method")

    def teardown_class(self):
        print("teardown class method")
