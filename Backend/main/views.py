from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Page d'acceuil du site web
def home(response):
    return HttpResponse("Page d'acceuil \n <ul> <li>Barre de recherche</li> <li>Login ou Create account</li></ul>"
                        "<a href=bookList>BookList</a> <a href=bookPage>BookPage</a> <a href=register>Creation de compte</a> <a href=administration>Page Admin</a>")

def bookList(response):
    return HttpResponse("Page affichant la liste de livres recherchés. <a href=/>Retour</a>")

def bookPage(response):
    return HttpResponse("Page spécifique à un livre dans une libraire. <ul><li>Affichage des informations sur le livre</li><li>Boutton pour pouvoir emprunter un livre</li>"
                        "<li>Section Commentaire</li></ul> <a href=/>Retour</a>")

def administration(response):
    return HttpResponse("Page que les admins vont accéder pour modifier/ajouter/supprimer des livres <a href=/>Retour</a>")