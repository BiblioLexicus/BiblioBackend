import os

from django.shortcuts import render
from main.models import UserList
from register.commands import *

# Create your views here.

default_dict = {"organisation_name": os.getenv("ORGANISATION_NAME")}


# models.py a une fonction userlist + username + email. On peut avoir accès a cela quand on crée django
def login(response):
    return render(response, "registration/login.html", {} | default_dict)


def register(request):
    creation = None

    response = render(
        request, "registration/register.html", {"creation": creation} | default_dict
    )

    if request.method == "POST":
        if request.POST.get("inscription_btn"):
            creation = creation_utilisateur(request)

            if creation:
                response = render(
                    request,
                    "registration/register.html",
                    {"creation": creation} | default_dict,
                )
                response.set_cookie("is_logged", True)  # Creation d'un cookie logged_in
                value_logged = request.COOKIES["is_logged"]

    return response
