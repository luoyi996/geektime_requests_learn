from dataclasses import dataclass
from typing import Any


@dataclass
class LoginParams:
    username: Any = None
    password: Any = None
