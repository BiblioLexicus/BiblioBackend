import datetime
import decimal

from main.models import UserList


def creation_utilisateur(request):

    # Vérifier que l'utilisateur est unique...

    name = request.POST.get("nom")
    prenom = request.POST.get("prenom")
    date_naissance = request.POST.get("dateNaissance")
    email = request.POST.get("email")
    passwordNotHash = request.POST.get("mdp")
    adress = request.POST.get("address")

    # modification de la date de publication:
    date_naissance = datetime.datetime.strptime(date_naissance, "%Y-%m-%d")

    try:
        user = UserList(
            id_users="2",  # Il faut créer la fonction qui genere le id du user
            password_hash=passwordNotHash,
            name=prenom,
            first_name=name,
            date_birth=date_naissance,
            fees=decimal.Decimal(1),  # Rajouter input pour les frais
            email=email,
            addresse_postale=adress,
            expiration_subscription=date_naissance,
            permissions="AA",  # Il faut changer cela pour une permission par defaut qui n'est pas Admin
            related_library_id="01",
        )  # Rajouter un input pour cette valeur

        user.save()
        print("success")
        return True

    except:
        print("erreur")
        return False
