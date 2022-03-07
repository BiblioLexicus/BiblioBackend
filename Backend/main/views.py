import os
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .commands import search_home

default_dict = {"organisation_name": os.getenv("ORGANISATION_NAME")}
organisation_name = os.getenv("ORGANISATION_NAME")


def home(response):
    # Page d'acceuil du site web

    if search_home(response) != "":
        recherche = search_home(response)
        return redirect('/search/'+str(recherche)) #Redirect l'utilisateur à la page de recherche en passant la recherche comme paramètre.

    return render(response, "main/acceuil.html", {} | default_dict)


def search(response, name):

    liste_livres = ['livre 1', 'livre 2', 'livre 3', 'livre 3']
    out_liste = []

    if name in liste_livres:
        for out in liste_livres:
            if out == name:
                out_liste.append(out)
    
    return render(response, "main/search.html", {"name": name, "liste_livres": out_liste} | default_dict)


def item(response, id):
    item_name = "Item"
    item_author = "Author"
    item_res = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore "
        "et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut "
        "aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse "
        "cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa "
        "qui officia deserunt mollit anim id est laborum. "
    )
    item_img = "https://cdn.discordapp.com/attachments/792090502760890379/945444402409664562/image_final_intro.png"
    item_edition = "Edition"
    item_publisher = "Publish"
    """return HttpResponse(
        "Page spécifique à un livre dans une libraire. <ul><li>Affichage des informations sur le "
        "livre</li><li>Boutton pour pouvoir emprunter un livre</li> <li>Section Commentaire</li></ul> "
        "id du livre: " + str(id)
    )"""
    return render(
        response,
        "main/item.html",
        {
            "item_img": item_img,
            "item_name": item_name,
            "item_res": item_res,
            "item_publisher": item_publisher,
            "item_edition": item_edition,
            "item_author": item_author,
        }
        | default_dict,
    )


def administration(response):

    # Vérifie si l'utilisateur est un adminstrateur
    # Accès à la liste de livre dans une librairie et peut ajouter/supprimer/modifier des livres

    liste_livres = ['livre 1', 'livre 2', 'livre 3', 'livre 3']
    out_liste = []


    if response.method == "GET":
        if response.GET.get("search"):
            recherche = response.GET.get("livre")

            if len(recherche) > 2:
                out_liste.clear()
                if recherche in liste_livres:
                    for out in liste_livres:
                        if out == recherche:
                            out_liste.append(out)              


    return render(response, 'main/administration.html', {"liste_livres": out_liste} | default_dict)


def profile(response):

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
    return HttpResponse("Page de settings de l'utilisateur.")


def panier(response):
    liste_emprunts = ["livre 1", "livre 2", "livre 3"]

    return render(
        response, "main/panier.html", {"liste_emprunts": liste_emprunts} | default_dict
    )


def librairie(response, id):
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
