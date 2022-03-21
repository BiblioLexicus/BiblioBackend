import math
import random
import sys


def intToid2Char(valInt):
    convertionTab = {
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
    valInt / 32
    id = (
        str(convertionTab.get(int(valInt / 32)))
        if valInt / 32 >= 10
        else str(int(valInt / 32))
    )

    id += (
        str(convertionTab.get(valInt % 32))
        if valInt % 32 > 9
        else str(int(valInt % 32))
    )
    print(valInt % 32)
    return id


def creationIdUnique():
    return math.pow(2, 32) * random.random()


# de la base 32 à l'int
def id2CharToInt(id_char):
    return int(id_char, 32)


# bookOrUser est un boolean qui si true alors book sinon user
def generalIdCreationAndManagement(
    valInt, bookOrUser, idPermission, idCategorie, idType
):
    thisId = ""
    if bookOrUser:
        thisId = intToid2Char(valInt) + idCategorie + idType + creationIdUnique()
    else:
        pass