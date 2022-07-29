from geektime_requests_learn.LiteMall.api.test_method import MallUserManage
import pytest

from geektime_requests_learn.LiteMall.utils.get_yaml_data import GetData
from geektime_requests_learn.LiteMall.utils.log import log

data = GetData().load_yaml('data/member_manage_query.yaml')


class TestMemberManageQuery:
    def setup_class(self):
        log().info(f'{self.setup_class.__name__} 初始化数据')
        self.member = MallUserManage(username='admin123', password='admin123')

    def setup(self):
        ...

    def teardown(self):
        ...

    def teardown_class(self):
        ...

    @pytest.mark.parametrize("username, mobile, user_id", data['query_params'])
    def test_member_query(self, username, mobile, user_id):
        """查询接口测试"""
        r = self.member.member_manage_search(username, mobile, user_id)
        assert r.status_code == 200
        assert r.json()["errno"] == 0
        assert r.json()["errmsg"] == "成功"

    @pytest.mark.parametrize('user_id, username', data["update_data"])
    def test_member_update(self, user_id, username):
        """查看user详情：更新信息接口"""
        r = self.member.member_manage_user_update(user_id, username)
        assert r.status_code == 200
        assert r.json()["errno"] == 0
        assert r.json()["errmsg"] == "成功"

