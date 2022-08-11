from dataclasses import asdict
from typing import List

import requests
from requests import Response

from geektime_requests_learn.homework.model.data_stream.lite_mall_token import LiteMallToken
from geektime_requests_learn.homework.model.data_stream.search_params import SearchParams
from geektime_requests_learn.homework.utils.log import log


class LiteMallSearch:
    def __init__(self):
        self.token = LiteMallToken().refresh_token('test123', 'test123')

    def search(self, content: SearchParams) -> (List, Response):
        r = requests.get(
            # url='http://litemall.hogwarts.ceshiren.com/wx/goods/list',
            url='https://litemall.hogwarts.ceshiren.com/wx/goods/list',
            headers={'X-Litemall-Token': self.token},
            json=asdict(content)
        )
        log().debug(f"{self.search.__name__} Method Msg: Search Value: {content}")
        log().debug(f"{self.search.__name__} Method Msg: Response Result: {r.json()}")
        if r.status_code == 200:
            if r.json()['errno'] == 0:
                return r.json()['data']['list']
        else:
            log().error(f"{self.search.__name__} Method Msg: Response Result: {r.status_code}")
            return r
