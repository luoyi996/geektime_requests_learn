from typing import List

import requests
from requests import Response

from geektime_requests_learn.homework.model.data_stream.lite_mall_token import LiteMallToken
from geektime_requests_learn.homework.utils.log import log


class ProductList:
    def __init__(self):
        self.token = LiteMallToken().refresh_token('test123', 'test123')

    def details(self, product_id) -> Response:
        r = requests.get(
            # url='http://litemall.hogwarts.ceshiren.com/wx/goods/detail',
            url='https://litemall.hogwarts.ceshiren.com/wx/goods/detail',
            headers={'X-Litemall-Token': self.token},
            params={'id': product_id}
        )
        log().debug(f"{self.details.__name__} Method Msg: Product ID: {product_id}")
        log().debug(f"{self.details.__name__} Method Msg: Response Result: {r.json()}")
        if r.status_code == 200:
            return r
        else:
            log().error(f'{self.details.__name__} Method Msg: Response Code: {r.status_code}')
            return r
