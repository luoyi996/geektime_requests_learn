import requests
from requests import Response

from geektime_requests_learn.homework.model.data_stream.login_params import LoginParams
from geektime_requests_learn.homework.utils.log import log


class Login:
    def user_login(self, params: LoginParams) -> Response:
        r = requests.post(
            # url='http://litemall.hogwarts.ceshiren.com/wx/auth/login',
            url='https://litemall.hogwarts.ceshiren.com/wx/auth/login',
            json={
                'username': params.username,
                'password': params.password,
            }
        )
        log().debug(f"{self.user_login.__name__} Method Msg: Login User Info: {params}")
        log().debug(f"{self.user_login.__name__} Method Msg: Response Result: {r.json()}")
        if r.status_code == 200:
            return r
        else:
            log().error(f"{self.user_login.__name__} Method Msg: Response Code: {r.status_code}")
            return r
