from dataclasses import dataclass
from typing import Any


@dataclass
class AddShoppingCartParams:
    goodsId: Any = None
    number: int = 1
    productId: Any = None
