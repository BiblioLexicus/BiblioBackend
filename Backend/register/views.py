import os

from django.shortcuts import render
from register.commands import *

# Create your views here.

default_dict = {"organisation_name": os.getenv("ORGANISATION_NAME")}


def login(request):
    """
    Login.
    TODO: models.py a une fonction userlist + username + email. On peut avoir accès a cela quand on crée django

    :param request:
    :return:
    """
    response = render(request, "registration/login.html", {"log": False} | default_dict)

    connexion_status = connexion(request)  # Contient des informations de connexion

    try:
        if connexion_status[0]:
            try:
                response = render(
                    request,
                    "registration/login.html",
                    {
                        "user": UserList.objects.filter(
                            email=str(request.POST.get("email"))
                        )[0],
                        "log": True,
                    }
                    | default_dict,
                )
                response.set_cookie("is_logged", True)
                response.set_cookie("id_user", connexion_status[1])
                return response
            except Exception as e:
                print(e)
                pass
    except Exception as e:
        print(e)
        pass

    return response


def register(request):
    """
    Enregistre un nouvel utilisateur.

    :param request:
    :return:
    """
    creation = None

    response = render(
        request, "registration/register.html", {"creation": creation} | default_dict
    )

    if request.method == "POST":
        if request.POST.get("inscription_btn"):
            creation = creation_utilisateur(request)
            response = render(
                request,
                "registration/register.html",
                {"creation": creation} | default_dict,
            )
            # response.set_cookie("is_logged", True)  Creation d'un cookie logged_in
            # value_logged = request.COOKIES["is_logged"] pour avoir la valeur d'un cookie

    return response


def logout(request):
    """
    Déconnexion d'un utilisateur.

    :param request:
    :return:
    """
    response = render(request, "registration/logout.html", {} | default_dict)

    response.set_cookie("is_logged", False)
    response.set_cookie("id_user", None)

    return response
