import datetime
from dataclasses import dataclass


@dataclass
class AddMember:
    username: str = None
    english_name: str = ''
    account: str = None
    biz_mail: str = None
    phone: int = None
    telephone: int = ''
    address: str = ''
    member_mail: str = ''
    position: str = ''

