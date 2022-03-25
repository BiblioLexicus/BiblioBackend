import os

from django.http import HttpResponse
from django.shortcuts import redirect, render

from .commands import *

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

    if len(search_home(response)) > 3 :
        recherche = search_home(response)
        print(recherche)
        return redirect("/search/" + str(recherche))

    out_liste = search_page_affichage(response, str(name))  # Liste de résultats

    return render(
        response,
        "main/search.html",
        {"name": name, "liste_livres": out_liste} | default_dict,
    )


def item(response, id):

    if search_home(response) != "":
        recherche = search_home(response)
        return redirect(
            "/search/" + str(recherche)
        )  # Redirect l'utilisateur à la page de recherche en passant la recherche comme paramètre.

    info_livre = affichage_item(response, id)  # Item specifique a afficher
    info_livre = info_livre[0]

    return render(
        response,
        "main/item.html",
        {"livre": info_livre} | default_dict,
    )


def administration(response):
    if search_home(response) != "":
        recherche = search_home(response)
        return redirect("/search/" + str(recherche))

    out = ""

    if response.method == "GET":
        if response.GET.get("searchAdmin"):
            recherche = response.GET.get("livre")
            out = administration_search(response, recherche)

    if response.method == "POST": #Si il y a une request POST, on envoie la requête à commands.py pour créer un livre.
        if response.POST.get("create"):
            create_book(response)

    return render(response, "main/administration.html", {"liste_livres": out} | default_dict)


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


def settings(response):
    if search_home(response) != "":
        recherche = search_home(response)
        print(recherche)
        return redirect(
            "/search/" + str(recherche)
        )  # Redirect l'utilisateur à la page de recherche en passant la recherche comme paramètre.
    return HttpResponse("Page de settings de l'utilisateur.")


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


def librairie(response, id):

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
