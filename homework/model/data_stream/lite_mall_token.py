from geektime_requests_learn.homework.api.login import Login
from geektime_requests_learn.homework.model.data_stream.login_params import LoginParams
from geektime_requests_learn.homework.utils.log import log


class LiteMallToken:
    def __init__(self):
        self.params = LoginParams()
        self.user = Login()

    def refresh_token(self, username, password):
        params = LoginParams()
        params.username = username
        params.password = password
        r = self.user.user_login(params)
        log().info(f'token = {r.json()["data"]["token"]}')
        return r.json()["data"]["token"]
