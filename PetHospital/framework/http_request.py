import json
from dataclasses import dataclass, field

import requests
from requests import Response as RequestsResponse


@dataclass
class Request:
    method: str = None
    host: str = None
    path: str = None
    params: dict = None
    data: dict = None
    headers: dict = field(default=dict)
    input_type: str = 'json'
    proxies: dict = None
    verify: bool = False

    def send(self):
        raw = None
        if self.input_type == 'json':
            self.headers = {"Content-Type": "application/json"}
            if self.data is None:
                raw = None
            else:
                raw = json.dumps(self.data)

        request = requests.request(
            method=self.method,
            url=self.host + self.path,
            params=self.params,
            data=raw,
            headers=self.headers,
            proxies=self.proxies,
            verify=self.verify
        )
        r = Response(request)
        return r


class Response:
    def __init__(self, requests_response):
        self.r: RequestsResponse = requests_response

    def json(self):
        return self.r.json()

    @property
    def status_code(self):
        return self.r.status_code
