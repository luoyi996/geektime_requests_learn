import requests
from requests import Response

from geektime_requests_learn.homework.model.data_stream.login_params import LoginParams
from geektime_requests_learn.homework.utils.log import log


class Login:
    def user_login(self, params: LoginParams) -> Response:
        r = requests.post(
            url='http://litemall.hogwarts.ceshiren.com/wx/auth/login',
            json={
                'username': params.username,
                'password': params.password,
            }
        )
        log().debug(f"Login info: {params}")
        log().debug(f"{self.user_login.__name__}::Response value: {r.json()}")
        return r
