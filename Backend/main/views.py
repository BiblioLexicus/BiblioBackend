from re import L
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Page d'acceuil du site web
def home(response):
    return HttpResponse("Page d'acceuil \n <ul> <li>Barre de recherche</li> <li>Connexion ou creation de compte</li></ul> "
                        "<a href=search/test>Search</a> <a href=item/1>Item</a> <a href=administration>Admin</a> <a href=profile>Profile</a> "
                        "<a href=profile/settings>Settings</a> <a href=panier>Panier</a> <a href=librairie/1>Librairie</a>")

def search(response, name):
    return HttpResponse("Page affichant la liste de livres recherchés. <a href=/>Retour</a> </br> Votre Recherche: " + name)

def item(response, id):
    return HttpResponse("Page spécifique à un livre dans une libraire. <ul><li>Affichage des informations sur le livre</li><li>Boutton pour pouvoir emprunter un livre</li>"
                        "<li>Section Commentaire</li></ul> id du livre: " + str(id))

def administration(response):
    return HttpResponse("Page que les admins vont accéder pour modifier/ajouter/supprimer des livres <a href=/>Retour</a>")

def profile(response):
    return HttpResponse("Page de profile de l'utilisateur.")

def settings(response):
    return HttpResponse("Page de settings de l'utilisateur.")

def panier(response):
    return HttpResponse("Panier de l'utilisateur.")

def librairie(response, id):
    return HttpResponse("Page de la librairie -> id: " + str(id))