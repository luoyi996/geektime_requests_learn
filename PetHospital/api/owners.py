from dataclasses import asdict
from typing import List

import requests
from requests import Response

from geektime_requests_learn.PetHospital.api.owner_data import Owner


class OwnersMethod:
    def search(self, lastName, key='lastName') ->List:
        r = requests.get(
            url='https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com:443/petclinic/api/owners',
            params={key: lastName},
        )
        if r.status_code == 200:
            owner_list = []
            for item in r.json():
                owner = Owner(**item)
                owner_list.append(owner)
            return owner_list
        else:
            return []

    def add(self, values) -> Response:
        r = requests.post(
            url='https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com:443/petclinic/api/owners',
            json=asdict(values)
        )
        return r

    def update(self):
        ...

    def get_pet_master(self, list_id) -> (str, Response):
        """查找宠物的主人"""
        r = requests.get(
            url=f'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com:443/petclinic/api/owners/{list_id}',
            headers={"Content-Type": "application/json"}
        )
        if r.status_code == 200:
            if r.json()["pets"] is not []:
                return r.json()["pets"][0]["name"]
            else:
                return "该宠物还没有主人"
        else:
            return r

    def delete(self, owner_id) -> Response:
        r = requests.request(
            method='delete',
            url=f'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com:443/petclinic/api/owners/{owner_id}'
        )
        return r

    def clear(self, lastName) -> None:
        for item in self.search(lastName):
            self.delete(item.id)
