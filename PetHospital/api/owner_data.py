import json
from dataclasses import dataclass


@dataclass
class Owner:
    address: str = None
    city: str = None
    firstName: str = None
    id: int = None
    lastName: str = None
    pets: list = None
    telephone: str = None
