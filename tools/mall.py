import random
from requests import Response
import requests


class Mall:
    def login(self, username, password, code) -> Response:
        r = requests.post(
            url='https://litemall.hogwarts.ceshiren.com/admin/auth/login',
            headers={"Origin": "https://litemall.hogwarts.ceshiren.com"},
            json={
                'username': username,
                'password': password,
                'code': code
            }
        )
        return r

    def get_token(self):
        """获取登录后的token值"""
        user_token = self.login(username='admin123', password='admin123', code='').json()['data']['token']
        cookies = {'X-Litemall-Admin-Token': user_token}
        return cookies

    def logout(self) -> Response:
        r = requests.post(
            url='https://litemall.hogwarts.ceshiren.com/admin/auth/logout',
            json={'token': f"{self.get_token().values()}"},
            cookies=self.get_token(),
            headers=self.get_token()
        )
        return r

    def user_addr(self) -> Response:
        r = requests.get(
            url='https://litemall.hogwarts.ceshiren.com/admin/address/list?page=1&limit=20&sort=add_time&order=desc',
            cookies=self.get_token(),
            headers=self.get_token(),
            verify=False

        )
        return r

    def first_page(self) -> Response:
        r = requests.get(
            url='https://litemall.hogwarts.ceshiren.com/admin/dashboard',
            cookies=self.get_token(),
            headers=self.get_token(),
            verify=False
        )
        return r

    def order_manage(self) -> Response:
        r = requests.get(
            url='https://litemall.hogwarts.ceshiren.com/admin/order/list'
                '?page=1&limit=20&sort=add_time&order=desc&start=&end=',
            cookies=self.get_token(),
            headers=self.get_token(),
            verify=False
        )
        return r

    def update_apple(self) -> Response:
        r = requests.post(
            url='https://litemall.hogwarts.ceshiren.com/admin/goods/update',
            cookies=self.get_token(),
            headers=self.get_token(),
            verify=False,
            json={
                "goods": {
                    "id": 1181061,
                    "goodsSn": "u001",
                    "name": "苹果",
                    "categoryId": 1027001,
                    "brandId": 1001002,
                    "gallery": [],
                    "keywords": None,
                    "brief": "一个红红并且好吃的苹果",
                    "isOnSale": True,
                    "sortOrder": 100,
                    "picUrl": "",
                    "isNew": True,
                    "isHot": False,
                    "unit": "’件‘",
                    "counterPrice": 230,
                    "retailPrice": 10,
                    "addTime": "2022-07-21 12:09:11",
                    "updateTime": "2022-07-21 12:09:11",
                    "deleted": False
                },
                "specifications": [
                    {
                        "id": 307,
                        "goodsId": 1181061,
                        "specification": "规格",
                        "value": "标准",
                        "picUrl": "",
                        "addTime": "2022-07-21 12:09:11",
                        "updateTime": "2022-07-21 12:09:11",
                        "deleted": False
                    }
                ],
                "products": [
                    {
                        "id": 308,
                        "goodsId": 1181061,
                        "specifications": [
                            "标准"
                        ],
                        "price": 10,
                        "number": 10,
                        "url": "",
                        "addTime": "2022-07-21 12:09:11",
                        "updateTime": "2022-07-21 12:09:11",
                        "deleted": False
                    }
                ],
                "attributes": []
            }
        )
        return r

    def create_banana(self) -> Response:
        commodity_id = "u" + str(random.randint(1, 100))
        commodity_name = "香蕉" + str(random.randint(1, 100))

        r = requests.post(
            url='https://litemall.hogwarts.ceshiren.com/admin/goods/create',
            cookies=self.get_token(),
            headers=self.get_token(),
            verify=False,
            json={
                "goods": {
                    "picUrl": "",
                    "gallery": [],
                    "isHot": False,
                    "isNew": True,
                    "isOnSale": True,
                    "goodsSn": f"{commodity_id}",
                    "name": f"{commodity_name}",
                    "categoryId": 1027001,
                    "brandId": 1001000,
                    "brief": "新鲜香蕉，产自广东",
                    "detail": "<p>海南成熟香蕉，好吃又好看还便宜</p>",
                    "counterPrice": "8"
                },
                "specifications": [
                    {
                        "specification": "规格",
                        "value": "标准",
                        "picUrl": ""
                    }
                ],
                "products": [
                    {
                        "id": 0,
                        "specifications": [
                            "标准"
                        ],
                        "price": "8",
                        "number": "10",
                        "url": ""
                    }
                ],
                "attributes": [
                    {
                        "attribute": "8元一斤",
                        "value": "8"
                    }
                ]
            }
        )
        return r

