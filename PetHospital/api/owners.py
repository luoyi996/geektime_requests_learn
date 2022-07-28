from dataclasses import asdict
from typing import List
from requests import Response
from geektime_requests_learn.PetHospital.api.owner_data import Owner
from geektime_requests_learn.PetHospital.framework.http_request import Request
from geektime_requests_learn.PetHospital.utils.get_data import GetData
from geektime_requests_learn.PetHospital.utils.log import log


class OwnersMethod:
    def __init__(self):
        # 对request库的一次封装
        self.yaml_data = GetData().load_yaml('data/env.yaml')
        self.request = Request()
        # 获取默认测试环境
        self.host = self.yaml_data[self.yaml_data["default"]]

    def search(self, lastName, key='lastName') -> List:
        self.request.method = 'get'
        self.request.host = self.host
        self.request.path = '/petclinic/api/owners'
        self.request.params = {key: lastName}
        r = self.request.send()
        if r.status_code == 200:
            owner_list = []
            for item in r.json():
                owner = Owner(**item)
                owner_list.append(owner)
            return owner_list
        else:
            return []

    def add(self, values):
        self.request.method = 'post'
        self.request.host = self.host
        self.request.path = '/petclinic/api/owners'
        self.request.input_type = 'json'
        self.request.data = asdict(values)
        r = self.request.send()
        return r

    def update(self):
        ...

    def get_pet_master(self, list_id) -> (str, int):
        """通过id查找宠物的主人"""
        self.request.method = 'get'
        self.request.host = self.host
        self.request.path = f'/petclinic/api/owners/{list_id}'
        r = self.request.send()
        if r.status_code == 200:
            if r.json() is not {}:
                if list_id == '':
                    return '查询出所有宠物的主人'
                return f"{r.json()['firstName']} {r.json()['lastName']}"
            else:
                return "该宠物还没有主人"
        else:
            return r.status_code

    def delete(self, owner_id) -> Response:
        self.request.method = 'delete'
        self.request.host = self.host
        self.request.path = f'/petclinic/api/owners/{owner_id}'
        r = self.request.send()
        if owner_id is '':
            log().info(f'输出所有信息：{r.json()}')
        return r

    def clear(self, lastName=None) -> None:
        for item in self.search(lastName):
            self.delete(item.id)
