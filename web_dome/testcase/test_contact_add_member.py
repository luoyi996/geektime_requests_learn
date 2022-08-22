import datetime
import pytest
from geektime_requests_learn.web_dome.page.home_page import HomePage
from geektime_requests_learn.web_dome.params_data import AddMember


class TestLogin:
    def setup_class(self):
        self.wework = HomePage()
        self.contact = self.wework.contact_page()

    def teardown_class(self):
        self.contact.close()

    @pytest.mark.parametrize('member_data', [
        {'username': 'user_01', 'account': 'ly_'},
        {'username': '罗毅', 'account': 'ly_'},
        {'username': 123456, 'account': 'ly_'},
    ])
    def test_add_member(self, member_data):
        timestamp = str(datetime.datetime.now().timestamp()).split('.')[1]
        member = AddMember(**member_data)
        if member.account is None:
            member.account = member.username
        member.account += timestamp
        if member.biz_mail is None:
            member.biz_mail = member.account
        member.phone = int('15078' + timestamp)
        self.contact.add_member(member)


