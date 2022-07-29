import json
from dataclasses import dataclass, field

import requests
from requests import Response

from geektime_requests_learn.LiteMall.utils.get_yaml_data import GetData
from geektime_requests_learn.LiteMall.utils.log import log


@dataclass
class HTTPRequest:
    method: str = None
    host: str = None
    path: str = None
    params: dict = None
    headers: dict = field(default=dict)
    data: dict = None
    proxies: dict = None
    verify: bool = False
    data_type: str = 'json'

    def send(self):
        host = GetData().load_yaml('data/env.yaml')
        self.host = host[host["default"]]
        raw = None
        if self.data_type == 'json':
            self.headers.update({"Content-Type": "application/json"})
            if self.data is None:
                raw = None
            else:
                raw = json.dumps(self.data)

        send_request = requests.request(
            method=self.method,
            url=self.host + self.path,
            params=self.params,
            headers=self.headers,
            data=raw,
            proxies=self.proxies,
            verify=self.verify
        )
        if self.params is not None:
            log().debug(f"请求数据：{self.params}")
        else:
            log().debug(f"请求数据：{raw}")
        r = HTTPResponse(send_request)
        log().debug(f"响应数据：{r.json()}")
        log().debug(f"响应码：{r.status_code}")
        return r


@dataclass
class HTTPResponse:
    def __init__(self, requests_response):
        self.r: Response = requests_response

    def json(self):
        return self.r.json()

    def unlock(self):
        """这里进行解锁逻辑"""
        ...

    @property
    def status_code(self):
        return self.r.status_code
