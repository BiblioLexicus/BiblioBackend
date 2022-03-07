import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

default_dict = {"organisation_name": os.getenv("ORGANISATION_NAME")}


def inscription(response):
    return HttpResponse("Page de création de compte <a href=/>Retour</a>")
