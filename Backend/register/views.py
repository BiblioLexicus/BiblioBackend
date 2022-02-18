from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inscription(response):
    return HttpResponse("Page de création de compte <a href=/>Retour</a>")

# Django s'occupe déja de la page de login. Il faut juste créer login.html dans templates/registration/