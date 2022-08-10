from dataclasses import dataclass
from typing import Any


@dataclass
class SearchParams:
    keyword: Any = None
    page: int = None
    limit: int = None

