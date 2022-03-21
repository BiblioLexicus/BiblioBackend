import os

from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import Rechercher
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
"""
def create_book():
    try:
"""
