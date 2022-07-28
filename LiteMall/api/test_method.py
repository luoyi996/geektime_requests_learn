from geektime_requests_learn.LiteMall.framework.http_request_protocol import HTTPRequest


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

    def get_token(self):
        ...