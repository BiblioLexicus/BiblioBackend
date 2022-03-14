from enum import Enum


class WorkCategoryEnums(Enum):
    AB = "Album et Journaux"
    AM = "Anime et Manga"
    dJ = "DVD Jeunes"
    da = "DVD Adolescents"
    dA = "DVD Adultes"
    DC = "Disque Compact"
    js = "Jeu de societe"
    JJ = "Jeu Video Jeunes"
    Ja = "Jeu Video Adolescents"
    JA = "Jeu Video Adultes"
    PJ = "Periodique Jeunes"
    PA = "Periodique Adultes"
    rJ = "Reference Jeunes"
    rA = "Reference Adultes"
    RJ = "Roman Jeunes"
    Ra = "Roman Adolescents"
    RA = "Roman Adultes"
    OO = "Autres"


class WorkTypeEnum(Enum):
    AA = "Action et Aventure"
    RD = "Romance et Drame"
    TH = "Thriller et Horreur"
    DA = "Ouvrage de style Documentaire"
    PS = "Policier et Suspense"
    EA = "Education et Apprentissage"
    CH = "Comedie et Humour"
    SL = "Sports et Loisirs"
    AR = "Action et Romance"
    TD = "Triller et Drame"
    CR = "Comedie et Romance"
    OO = "Autres"
