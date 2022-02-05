import datetime
from typing import List, Optional

from Comment import Comment
from Item import Item
from Permission import Permission


class User:
    """Users"""

    id: int
    name: str
    mdp: str
    date_joined: datetime.datetime


class Usager(User):
    profile: str
    address: Optional[str]
    loans: List[Item]
    reservations: List[Item]
    comments: Optional[List[Comment]]
    print_fees: float
    delay_fees: float
    other_fees: float


class Admin(User):
    permissions: List[Permission]
    library_id: Optional[int]
