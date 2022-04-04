import os

from django.http import HttpResponse
from django.shortcuts import render
#from django.contrib.auth.forms import UserCreationForm
# Create your views here.

default_dict = {"organisation_name": os.getenv("ORGANISATION_NAME")}

# models.py a une fonction userlist + username + email. On peut avoir accès a cela quand on crée django
def inscription(response):
    return HttpResponse("Page de création de compte <a href=/>Retour</a>")

