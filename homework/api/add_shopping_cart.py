from dataclasses import asdict
from typing import List

import requests
from requests import Response

from geektime_requests_learn.homework.model.data_stream.add_shopping_cart_params import AddShoppingCartParams
from geektime_requests_learn.homework.model.data_stream.lite_mall_token import LiteMallToken
from geektime_requests_learn.homework.utils.log import log


class AddShoppingCart:
    def __init__(self):
        self.token = LiteMallToken().refresh_token('test123', 'test123')

    def add_shopping_cart(self, params: AddShoppingCartParams) -> Response:
        r = requests.post(
            # url='http://litemall.hogwarts.ceshiren.com/wx/cart/add',
            url='https://litemall.hogwarts.ceshiren.com/wx/cart/add',
            headers={'X-Litemall-Token': self.token},
            json=asdict(params)
        )
        log().debug(f"{self.add_shopping_cart.__name__} Method Msg: Add Shopping Info: {params}")
        log().debug(f"{self.add_shopping_cart.__name__} Method Msg: Response Result: {r.json()}")
        if r.status_code == 200:
            return r
        else:
            log().error(f"{self.add_shopping_cart.__name__} method msg: Response Code: {r.status_code}")
            return r

    def get_shopping_cart_list(self) -> List:
        r = requests.get(
            # url='http://litemall.hogwarts.ceshiren.com/wx/cart/index',
            url='https://litemall.hogwarts.ceshiren.com/wx/cart/index',
            headers={'X-Litemall-Token': self.token},
        )
        log().debug(f"{self.get_shopping_cart_list.__name__} Method Msg: Response Result: {r.json()}")
        if r.status_code == 200:
            return r.json()["data"]["cartList"]
        else:
            log().error(f"{self.get_shopping_cart_list.__name__} method msg: Response Code: {r.status_code}")
            return []

    def delete_shopping_cart(self, product_id) -> Response:
        r = requests.post(
            url='https://litemall.hogwarts.ceshiren.com/wx/cart/delete',
            json={'productIds': product_id},
            headers={'X-Litemall-Token': self.token}
        )
        log().debug(f"{self.delete_shopping_cart.__name__} Method Msg: Request Params: {product_id}")
        log().debug(f"{self.delete_shopping_cart.__name__} Method Msg: Response Result: {r.json()}")
        if r.status_code == 200:
            return r
        else:
            log().error(f"{self.delete_shopping_cart.__name__} Method Msg: Response Code: {r.status_code}")
            return r

    def clear_shopping_cart(self):
        cart_count = [i['productId'] for i in self.get_shopping_cart_list()]
        if len(cart_count) == 0:
            log().info(f"{self.clear_shopping_cart.__name__}: Shopping cart is not product")
        else:
            self.delete_shopping_cart(cart_count)
            log().info(f"{self.clear_shopping_cart.__name__}: Shopping cart list = "
                       f"{[i['productId'] for i in self.get_shopping_cart_list()]}")

