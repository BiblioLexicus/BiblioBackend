import decimal
import hashlib
from datetime import datetime

from django.db.models.query import QuerySet
from main.IDManagement import *
from main.models import UserList


def verification_existence(email: str) -> QuerySet:
    """
    Verifie si un utilisateur avec un email existe deja

    :param email:
    :return:
    """
    return UserList.objects.filter(email=email).exists()


def creation_utilisateur(request) -> bool:
    """
    Créé un utilisateur.

    :param request:
    :return:
    """
    # Vérifier que l'utilisateur est unique...

    name = request.POST.get("nom")
    prenom = request.POST.get("prenom")
    date_naissance = request.POST.get("dateNaissance")
    email = request.POST.get("email")
    passwordNotHash = request.POST.get("mdp")
    adress = request.POST.get("address")

    # modification de la date de publication:
    date_naissance = datetime.strptime(date_naissance, "%Y-%m-%d")
    expiration_subscription = datetime.strptime("3000-12-12", "%Y-%m-%d")
    user_id = generalIdCreationAndManagement(1, False, "AA", None, None)
    hashedPwd = hashlib.sha256(bytes(passwordNotHash, encoding="utf-8")).hexdigest()

    if not verification_existence(email):
        try:
            user = UserList(
                id_users=user_id,  # Il faut créer la fonction qui genere le id du user
                password_hash=hashedPwd,
                name=prenom,
                first_name=name,
                date_birth=date_naissance,
                fees=decimal.Decimal(1),  # Rajouter input pour les frais
                email=email,
                addresse_postale=adress,
                expiration_subscription=expiration_subscription,
                permissions="AA",  # Il faut changer cela pour une permission par defaut qui n'est pas Admin
                related_library_id="01",
            )  # Rajouter un input pour cette valeur
            user.save()
            return True

        except Exception as e:
            print(e)
            return False
    else:
        print("user exist")
        return False


def connexion(request) -> (bool, UserList):
    """
    Connexion de l'utilisateur à son compte

    :param request:
    :return:
    """
    try:
        email = request.POST.get("email")
        passwordNotHashed = request.POST.get("mdplogin")

        hashedPwd = hashlib.sha256(
            bytes(passwordNotHashed, encoding="utf-8")
        ).hexdigest()

        if hashedPwd == UserList.objects.filter(email=email)[0].password_hash:
            return (
                True,
                UserList.objects.filter(email=email)[0].id_users,
            )  # return true si logged in

        return False  # return false si erreur de connexion

    except Exception as e:
        print(e)
        return False, None
