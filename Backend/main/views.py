import os
from typing import Optional

from django.shortcuts import redirect, render
from django.utils.html import escape

from .commands import *
from .IDEnums import *
from .models import LibrariesData

default_dict = {
    "organisation_name": os.getenv("ORGANISATION_NAME"),
    "libraries": LibrariesData.objects.all(),
}
organisation_name = os.getenv("ORGANISATION_NAME")


def home(response):
    """
    Page d'acceuil.

    :param response:
    :return:
    """
    # Page d'acceuil du site web

    return render(response, "main/acceuil.html", {} | default_dict)

def advancedsearch(response):
    """
    Page d'acceuil.

    :param response:
    :return:
    """
    # Page d'acceuil du site web

    return render(response, "main/advancedsearch.html", {} | default_dict)


def search(response, name: Optional[str] = ""):
    """
    Search for an item.

    :param response:
    :param name: The name of the item
    :return:
    """
    name = escape(name)

    recherche = search_home(response)
    if recherche:
        print(recherche)
        return redirect("/search/" + str(recherche))

    out_liste = search_item_by_name(name=name)  # Liste de résultats

    return render(
        response,
        "main/search.html",
        {"name": name, "liste_livres": out_liste} | default_dict,
    )


def item(response, item_id):
    """


    :param response:
    :param item_id:
    :return:
    """
    state_of_emprunt = None

    info_livre = search_precise_item(item_id)  # Item specifique à afficher
    info_livre = info_livre[0]

    if response.method == "GET":
        if response.GET.get("emprunt"):
            if response.COOKIES["is_logged"] == "True":
                state_of_emprunt = emprunter(response)

    if response.method == "POST":  # Ajout d'un commentaire
        if response.POST.get("commSave"):
            ajouter_commentaire(response)

    liste_commentaires = voir_commentaire(response, item_id)
    liste_users = []

    for com in liste_commentaires:
        user = com.id_users
        tuple_comms = (user.name, com)
        liste_users.append(tuple_comms)

    print(liste_users)
    return render(
        response,
        "main/item.html",
        {
            "livre": info_livre,
            "state_of_emprunt": state_of_emprunt,
            "list_user": liste_users,
        }
        | default_dict,
    )


def administration(response):
    """
    TODO

    :param response:
    :return:
    """
    try:
        id_user = response.COOKIES["id_user"]
    except KeyError:
        return redirect("/")  # L'utilisateur n'est pas connecté

    user = UserList.objects.filter(id_users=id_user)

    if (user.exists() and user[0].permissions != "AA") or (
        not user.exists()
    ):  # verifie que l'utilisateur est admin
        return redirect("/")

    liste_info = [
        "nomLivre",
        "authorName",
        "datePublication",
        "editionHouse",
        "nbrPage",
        "resume",
        "genre",
        "language",
        "etat",
        "numeroCopie",
        "typeLivre",
        "price",
    ]
    creation = None
    out = ""
    edit_book = ""
    date_str = ""
    genre = ""
    etat = ""
    type_edit = ""
    are_we_editing = False
    etat_id = 0

    if response.method == "GET":
        if response.GET.get("searchAdmin"):
            recherche = response.GET.get("livre")
            out = administration_search(recherche)

    if response.method == "POST":
        # Si il y a une request POST, on envoie la requête à commands.py pour créer un livre.
        if response.POST.get("create"):
            creation = create_item(response, liste_info)
        if response.POST.get("Supprimer"):
            delete_item(response)

        if response.POST.get("Modifier"):
            work = response.POST.get("id_work")
            edit_book = search_precise_item(
                str(work)
            )[0]
            date_str = edit_book.publication_date.strftime("%Y-%m-%d")
            genre = str(WorkCategoryEnums[edit_book.genre].value)
            etat = str(
                "Bon" if int.from_bytes(edit_book.state, "big") == 1 else "Mauvais"
            )
            type_edit = str(WorkTypeEnum[edit_book.type_work].value)
            are_we_editing = True
            etat_id = int(1 if int.from_bytes(edit_book.state, "big") == 1 else 0)

        if response.POST.get("edit"):
            edit_item(response, liste_info)

    return render(
        response,
        "main/administration.html",
        {
            "liste_livres": out,
            "creation": creation,
            "edit_book": edit_book,
            "date_str": date_str,
            "genre": genre,
            "etat": etat,
            "type": type_edit,
            "edit_mode": are_we_editing,
            "etat_id": etat_id,
        }
        | default_dict,
    )


def profile(request):
    """


    :param request:
    :return:
    """

    log = request.COOKIES["is_logged"]
    user = None
    liste_emprunts = None

    if log == "True":
        log = True
    else:
        log = False

    id_user = request.COOKIES["id_user"]

    if log:
        liste_emprunts = search_emprunt(id_user)
        user = UserList.objects.filter(id_users=id_user)[0]

    response = render(
        request,
        "main/profil.html",
        {
            "user": user,
            "liste_emprunts": liste_emprunts,
            "log": log,
        }
        | default_dict,
    )

    return response


def panier(response):
    """


    :param response:
    :return:
    """
    user = get_user(response)
    liste_emprunts = LoanedWorks.objects.filter(id_users=user.id_users)

    return render(
        response, "main/panier.html", {"liste_emprunts": liste_emprunts} | default_dict
    )


def librairie(response, library_id: str):
    """
    Point d'entrée pour visionner les informations à propos d'une librairie.

    :param response: Requête de l'utilisateur.
    :param library_id: L'ID de la librairie.
    :return: Les informations à propos d'une librairie.
    """
    library_id = escape(library_id)
    libr = LibrariesData.objects.filter(id_library=library_id)[0]

    return render(
        response,
        "main/librairie.html",
        {"libr": libr} | default_dict,
    )


def settings(response):
    """
    Page de paramètres de l'utilisateur.

    :param response: La requête.
    :return: La page de paramètres de l'utilisateur.
    """
    try:
        id_user = response.COOKIES["id_user"]
    except KeyError:
        return redirect("/")

    user = UserList.objects.filter(id_users=id_user)[0]

    lst_genre = [genre.value for genre in WorkTypeEnum]
    return render(
        response,
        "main/usersettings.html",
        {"user": user, "lst_genre": lst_genre} | default_dict,
    )
