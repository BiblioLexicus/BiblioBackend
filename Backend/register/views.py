import os

from django.shortcuts import redirect, render
from main.models import UserList
from register.commands import *

# Create your views here.

default_dict = {"organisation_name": os.getenv("ORGANISATION_NAME")}


# models.py a une fonction userlist + username + email. On peut avoir accès a cela quand on crée django
def login(request): 
    response = render(
        request, "registration/login.html", {"log": False} | default_dict
    )

    connexion_status = connexion(request) # Contient des informations de connexion

    if connexion_status[0]: 
        try: 
            response = render(
                request, "registration/login.html", {"user": UserList.objects.filter(email=str(request.POST.get('email')))[0], "log": True} | default_dict
            )
            response.set_cookie('is_logged', True)
            response.set_cookie('id_user', connexion_status[1])
            return response
        except: 
            pass

    return response

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
                #response.set_cookie("is_logged", True)  Creation d'un cookie logged_in
                #value_logged = request.COOKIES["is_logged"] pour avoir la valeur d'un cookie

    return response

def logout(request): 
    response = render(
        request, "registration/logout.html", {} | default_dict
    )

    response.set_cookie("is_logged", False)
    response.set_cookie("id_user", None)

    return response