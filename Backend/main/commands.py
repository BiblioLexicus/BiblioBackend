import os
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import Rechercher

# Fonction pour faire de la recherche dans la page d'Acceuil
def search_home(response):
    if response.method == "GET": 
        if response.GET.get("search"): 
            recherche = response.GET.get("livre")
            return recherche # return la valeur recherché
    return ""