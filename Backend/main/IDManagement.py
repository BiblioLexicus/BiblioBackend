import math
import random


def intToid2Char(val_int):
    """
    ???

    :param val_int:
    :return:
    """
    convertion_tab = {
        10: "a",
        11: "b",
        12: "c",
        13: "d",
        14: "e",
        15: "f",
        16: "g",
        17: "h",
        18: "i",
        19: "j",
        20: "k",
        21: "l",
        22: "m",
        23: "n",
        24: "o",
        25: "p",
        26: "q",
        27: "r",
        28: "s",
        29: "t",
        30: "u",
        31: "v",
    }
    val_int / 32
    final_id = (
        str(convertion_tab.get(int(val_int / 32)))
        if val_int / 32 >= 10
        else str(int(val_int / 32))
    )

    final_id += (
        str(convertion_tab.get(val_int % 32))
        if val_int % 32 > 9
        else str(int(val_int % 32))
    )
    print(val_int % 32)
    return final_id


def creationIdUnique():
    """
    Retourne un ID unique

    :return: Un nombre aléatoire entre 2² et 2^32.
    """
    return math.floor(
        (math.pow(2, 32) * random.random())
    )  # return un int avec math.floor()


# de la base 32 à l'int
def id2CharToInt(id_char):
    return int(id_char, 32)


def generalIdCreationAndManagement(
    val_int, book_or_user, id_permission, id_categorie, id_type
) -> str:
    """
    Creates an ID for a book and user

    :param val_int:
    :param book_or_user: True if a book, False for a user
    :param id_permission:
    :param id_categorie:
    :param id_type:
    :return:
    """
    final_id: str
    if book_or_user:
        final_id = (
            str(intToid2Char(val_int))
            + " "
            + str(id_categorie)
            + " "
            + str(id_type)
            + " "
            + str(hex(creationIdUnique())[2:])
            + " "
            + "00"
        )
    else:
        final_id = (
            str(intToid2Char(val_int))
            + " "
            + str(hex(creationIdUnique())[2:])
            + " "
            + str(id_permission)
        )
    return final_id


def additionOfMultipleSameBooks(last_object_id: str):
    """
    ???

    :param last_object_id:
    :return:
    """

    this_id = last_object_id.split()
    this_id[len(this_id) - 1] = "0" + str(int(this_id[len(this_id) - 1]) + 1)
    print(this_id)
    print(" ".join(this_id))

    return " ".join(this_id)
