from django.shortcuts import render
from main.models import UserList
from main.views import default_dict
from register.commands import connexion, creation_utilisateur

# Create your views here.


def login(request):
    """
    Login.

    :param request: La requête Django
    :return: La page de login
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

    :param request: La requête Django
    :return: La page d'enregistrement
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

    :param request: La requête Django
    :return: La page de logout
    """
    response = render(request, "registration/logout.html", {} | default_dict)

    response.set_cookie("is_logged", False)
    response.set_cookie("id_user", None)

    return response
