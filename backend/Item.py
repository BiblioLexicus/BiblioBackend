import datetime
from typing import List, Optional

from Comment import Comment
from Loan import Loan


class Item:
    """
    An item that can be loaned or not.
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
