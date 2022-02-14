import datetime
from typing import List, Optional
from enum import Enum

from django.contrib.auth.models import User
from django.db import models


class Permission(Enum):
    """
    Permissions:
    ADMIN -> Can do everything
    LIBRARY_MANAGEMENT -> Can manage everything in a particular library
    ITEM_MANAGEMENT -> Can manage all items
    USER_MANAGEMENT -> Can manage all Users
    """

    ADMIN = 0
    LIBRARY_MANAGEMENT = 1
    ITEM_MANAGEMENT = 2
    USER_MANAGEMENT = 3


class Loan:
    """
    A loan of an item
    """

    id: int
    user_id: int
    book_id: int
    origin_library_id: int
    final_library_id: int
    loan_date: datetime.datetime
    return_date: datetime.datetime


class Comment(models):
    """A comment of an Item."""

    id: int
    author_id: int
    book_id: int
    description: str


class Transaction:
    id: int
    user_id: int
    item_id: int
    transaction_date: datetime.datetime


class Item(models):
    """An item that can be loaned or not.

    """

    id: int
    uuid: int
    name: str
    author: str
    publishing_house: str
    description: str
    Genre: List[str]
    rating: float
    publication_date: datetime.datetime
    added_date: datetime.datetime
    comments: Optional[List[Comment]]
    loan_history: Optional[List[Loan]]
    is_taken: bool
    is_reserved: bool
    is_loanable: bool
    libraries_id: List[int]
    loaner_id: int


class Book(Item):
    pages_number: int


class Movie(Item):
    length_hour: int
    length_minutes: int


class VideoGame(Item):
    platform: str


class Client(User):
    """A normal client.

    Base client class.
    """
    name: str
    mdp: str
    date_joined: datetime.datetime
    profile: str
    address: Optional[str]
    loans: List[Item]
    reservations: List[Item]
    loan_history: List[int]
    comments: Optional[List[Comment]]
    print_fees: float
    delay_fees: float
    other_fees: float

    def to_dict(self, user: User) -> dict:
        us = {
            'id': self.name,
            'name': self.name,
            'date_joined': self.date_joined,
            'profile': self.profile,

        }

        return us


class Admin(Client):
    permissions: List[Permission]
    library_id: Optional[int]

    def to_dict(self, user: User) -> dict:
        us = super(Admin, self).to_dict()

        us.update({
            'permissions': [permission for permission in self.permissions],
            'library_id': self.library_id
        })

        if user.has_perm(perm=Permission.USER_MANAGEMENT) or user.has_perm(perm=Permission.ADMIN):
            us.update({
                'mdp': self.mdp
            })

        return us


class Library(models):
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
