import datetime
import decimal
import os

from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import Rechercher
from .IDEnums import *
from .IDManagement import *
from .models import *


# Fonction pour faire de la recherche dans la page d'Acceuil
def search_home(response):
    if response.method == "GET":
        if response.GET.get("search"):
            recherche = response.GET.get("livre")
            return recherche  # return la valeur recherchée
    return ""


# Fonction pour afficher la liste des recherches sur la page search.html
def search_page_affichage(response, name):
    liste_livres = WorkList.objects.all().filter(name_works=name)

    return liste_livres


# Fonction pour afficher des informations sur un ouvrage précis
def affichage_item(response, id):
    livre = WorkList.objects.all().filter(id_works=id)

    return livre


# Fonction qui sert a faire la recherche dans la page d'administration
def administration_search(response, query):
    # faire en sorte de passer des parametres ex: User: <username>, Ouvrage: <Nom ouvrage>
    recherche = WorkList.objects.all().filter(name_works=query)

    return recherche


# Fonction pour la page de recherche avance qui va permettre a l'utilisateur d'avoir un resultat plus precis.
def recherche_avance():
    pass


# Fonction pour créer un livre
def create_book(response, liste_info):
    if response.method == "POST":

        for info in liste_info: #Vérifie que tout les éléments ont une longeur d'au moins 3.
            if len(str(response.POST.get(str(info)))) < 3 and info != "price" and info != "numeroCopie" and info != "nbrPage":
                return False # Si il y a une erreur retourne False

        try:
            nom_livre = response.POST.get("nomLivre")
            author_name = response.POST.get("authorName")
            date_publication = response.POST.get("datePublication")
            edition_house = response.POST.get("editionHouse")
            nombre_page = response.POST.get("nbrPage")
            resume = response.POST.get("resume")
            genre = response.POST["dropdown_genre"]
            language = response.POST.get("language")
            etat = response.POST["dropdown_etat"]
            numero_copie = response.POST.get("numeroCopie")
            type_livre = response.POST["dropdown_type"]
            price = response.POST.get("price")

            # modification de la date de publication:
            date_publication_list = date_publication.split("-")
            date_publication = datetime.date(
                int(date_publication_list[0]),
                int(date_publication_list[1]),
                int(date_publication_list[2]),
            )

            # Création de l'id (Pour l'instant j'ai fait des enum par défaut en attendant que je finisse le html avec les
            # bandes déroulantes)
            val_id = str(
                generalIdCreationAndManagement(
                    10, True, PermissionEnums.AA, genre, type_livre
                )
            )
            # Création de l'objet
            livre = WorkList(
                id_works=val_id,
                name_works=str(nom_livre),
                author_name=str(author_name),
                publication_date=date_publication,
                edition_house=str(edition_house),
                length=int(nombre_page),
                resume=str(resume),
                genre=str(genre),
                language=str(language),
                state=int(etat),
                copy_number=int(numero_copie),
                type_work=str(type_livre),
                price=decimal.Decimal(price),
            )
            livre.save()  # Enregistrement de l'objet
            return True #Retourne True si il le livre est créé. 
        except:
            return False #Retroune False si le livre n'est pas créé. 
