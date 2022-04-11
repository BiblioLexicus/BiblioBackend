import os

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render

from .commands import *
from .IDEnums import *

default_dict = {"organisation_name": os.getenv("ORGANISATION_NAME")}
organisation_name = os.getenv("ORGANISATION_NAME")


def home(response):
    # Page d'acceuil du site web

    if search_home(response) != "":
        recherche = search_home(response)
        print(recherche)
        return redirect(
            "/search/" + str(recherche)
        )  # Redirect l'utilisateur à la page de recherche en passant la recherche comme paramètre.

    return render(response, "main/acceuil.html", {} | default_dict)


def search(response, name):
    recherche = ""
    if len(search_home(response)) > 3:
        recherche = search_home(response)
        print(recherche)
        return redirect("/search/" + str(recherche))

    out_liste = search_page_affichage(recherche)  # Liste de résultats

    return render(
        response,
        "main/search.html",
        {"name": name, "liste_livres": out_liste} | default_dict,
    )


def item(response, item_id):
    if search_home(response) != "":
        recherche = search_home(response)
        return redirect(
            "/search/" + str(recherche)
        )  # Redirect l'utilisateur à la page de recherche en passant la recherche comme paramètre.

    info_livre = affichage_item(item_id)  # Item specifique à afficher
    info_livre = info_livre[0]

    return render(
        response,
        "main/item.html",
        {"livre": info_livre} | default_dict,
    )


def administration(response):
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

    if search_home(response) != "":
        recherche = search_home(response)
        return redirect("/search/" + str(recherche))

    if response.method == "GET":
        if response.GET.get("searchAdmin"):
            recherche = response.GET.get("livre")
            out = administration_search(recherche)

    if (
        response.method == "POST"
    ):  # Si il y a une request POST, on envoie la requête à commands.py pour créer un livre.
        if response.POST.get("create"):
            creation = create_book(
                response, liste_info
            )  # Creation est un boolean: (True si le livre est créé) (False si le livre n'est pas créé)
        if response.POST.get("Supprimer"):
            supprimer_livre(response)

        if response.POST.get("Modifier"):
            edit_book = search_book_by_id(response)[0]
            date_str = edit_book.publication_date.strftime("%Y-%m-%d")
            genre = str(WorkCategoryEnums[edit_book.genre].value)
            etat = str(
                "Bon" if int.from_bytes(edit_book.state, "big") == 1 else "Mauvais"
            )
            type_edit = str(WorkTypeEnum[edit_book.type_work].value)
            are_we_editing = True
            etat_id = int(1 if int.from_bytes(edit_book.state, "big") == 1 else 0)

        if response.POST.get("edit"):
            edit_book_admin(response, liste_info)

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


def profile(response):
    if search_home(response) != "":
        recherche = search_home(response)
        print(recherche)
        return redirect(
            "/search/" + str(recherche)
        )  # Redirect l'utilisateur à la page de recherche en passant la recherche comme paramètre.
    second_name = "Test"
    first_name = "Test"
    adress = "Bois de Boulogne"
    phone_number = "+1 (514) 514-5140"
    expiration_date = "23/02/01"

    liste_emprunts = ["emprunt1", "emprunt2", "emprunt3"]

    return render(
        response,
        "main/profil.html",
        {
            "second_name": second_name,
            "first_name": first_name,
            "adress": adress,
            "phone_number": phone_number,
            "expiration>_date": expiration_date,
            "liste_emprunts": liste_emprunts,
        }
        | default_dict,
    )


def panier(response):
    if search_home(response) != "":
        recherche = search_home(response)
        print(recherche)
        return redirect(
            "/search/" + str(recherche)
        )  # Redirect l'utilisateur à la page de recherche en passant la recherche comme paramètre.

    liste_emprunts = ["livre 1", "livre 2", "livre 3"]

    return render(
        response, "main/panier.html", {"liste_emprunts": liste_emprunts} | default_dict
    )


def librairie(response, library_id):
    if search_home(response) != "":
        recherche = search_home(response)
        print(recherche)
        return redirect(
            "/search/" + str(recherche)
        )  # Redirect l'utilisateur à la page de recherche en passant la recherche comme paramètre.

    librairie_nom = "Bibliothèque de Montreal"
    adresse = "rue de montreal"
    heures_ouverture = "8am à 9pm"

    return render(
        response,
        "main/librairie.html",
        {
            "librairie_nom": librairie_nom,
            "adresse": adresse,
            "heures_ouverture": heures_ouverture,
        }
        | default_dict,
    )


def settings(response):
    user = {
        "name": "Jean-jacques",
        "email": "jean@jacques.a",
        "postalCode": "AAA334",
        "imagelink": "",
    }
    lst_genre = [genre.value for genre in WorkTypeEnum]
    return render(
        response,
        "main/usersettings.html",
        {"user": user, "lst_genre": lst_genre} | default_dict,
    )
