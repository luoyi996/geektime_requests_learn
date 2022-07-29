from geektime_requests_learn.LiteMall.framework.http_request_protocol import HTTPRequest
from geektime_requests_learn.LiteMall.utils.log import log


class MallLoginMethod:
    def __init__(self):
        self.usr_login = HTTPRequest()

    def login(self, username, password, code):
        self.usr_login.method = 'post'
        self.usr_login.path = '/admin/auth/login'
        self.usr_login.headers = {"Origin": "https://litemall.hogwarts.ceshiren.com"}
        self.usr_login.data = {
            'username': username,
            'password': password,
            'code': code
        }
        r = self.usr_login.send()
        return r

    def get_token(self, username, password, code=''):
        r = self.login(username, password, code)
        if r.status_code == 200:
            if r.json()["data"]["adminInfo"]["nickName"] == username:
                return r.json()["data"]["token"]
            else:
                log().error(f"登录账号错误：{username}")
        else:
            log().error(f"{username}登录错误：{r.status_code}")


class MallUserManage:
    def __init__(self, username, password, code=''):
        """初始化场景，传入已经登录的账号和密码获取token"""
        self.user = HTTPRequest()
        self.token = MallLoginMethod().get_token(username, password, code)

    def member_manage_search(self, username, mobile, user_id, page=1, limit=20):
        self.user.method = 'get'
        self.user.path = '/admin/user/list'
        self.user.params = {
            'page': page,
            'limit': limit,
            'username': username,
            'mobile': mobile,
            'userId': user_id,
            'sort': 'add_time',
            'order': 'desc'
        }
        self.user.headers = {'X-Litemall-Admin-Token': self.token}
        r = self.user.send()
        return r

    def member_manage_user_update(self, user_id, username=None):
        """通过用户id查询用户信息"""
        data = self.member_manage_search(username=username, user_id=user_id, mobile=None).json()['data']
        self.user.method = "post"
        self.user.path = '/admin/user/update'
        self.user.headers = {'X-Litemall-Admin-Token': self.token}
        if len(data["list"]) == 1:
            self.user.data = data
        else:
            self.user.data = data['list'][0]
            log().error(f'{self.member_manage_search.__name__}通过id搜索值不唯一，一个id指向多个用户,此处取值为{data["list"][0]}')
        r = self.user.send()
        return r

    def mall_add_manage(self):
        ...


