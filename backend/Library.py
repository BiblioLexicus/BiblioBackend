import datetime
from typing import List, Optional

from Item import Item
from Transaction import Transaction
from User import Admin


class Library:
    """Library"""

    id: int
    name: str
    description: str
    location: Optional[str]
    opening_hour: Optional[datetime.datetime]
    closing_hour: Optional[datetime.datetime]
    opening_day: Optional[List[datetime.datetime]]
    closing_day: Optional[List[datetime.datetime]]
    items: List[Item]
    managers: List[Admin]
    transactions: List[Transaction]
