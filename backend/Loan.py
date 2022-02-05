import datetime


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
