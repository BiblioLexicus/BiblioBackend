from enum import Enum


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
