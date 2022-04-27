import decimal
from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db.models.query import QuerySet
from django.shortcuts import redirect

from .IDEnums import *
from .IDManagement import *
from .models import LoanedWorks, UserList, WorkList


def emprunter(response):
    """
    Emprunter un item.

    :param response:
    :return:
    """
    user_id = response.COOKIES["id_user"]
    user = UserList.objects.filter(id_users=user_id)[0]

    if LoanedWorks.objects.filter(id_users=user).exists():
        return False

    else:
        loan = LoanedWorks(
            id_works=WorkList.objects.filter(id_works=response.GET.get("id_work"))[0],
            end_loan_date=datetime.now() + relativedelta(months=1),
            id_users=user,
            work_lost=int(0),
        )

        loan.save()
        return True


def search_emprunt(user_id):
    """
    Trouve les items qui ont été empruntés par un utilisateur

    :param user_id:
    :return:
    """
    user = UserList.objects.filter(id_users=str(user_id))[0]
    liste_emprunts = LoanedWorks.objects.filter(id_users=user)

    liste_final = []

    for livre in liste_emprunts: # Permet de prendre le livre dans le loaned works et non le loaned works. 
        liste_final.append(livre.id_works)

    return liste_final


def search_home(response):
    """
    recherche dans la page d'Acceuil????

    :param response:
    :return:
    """
    if response.method == "GET":
        if response.GET.get("search"):
            recherche = response.GET.get("livre")
            return recherche  # return la valeur recherchée
    return ""


def search_item_by_name(name: str) -> QuerySet:
    """
    Cherche l'item.

    :param name:
    :return:
    """
    list_items: QuerySet = WorkList.objects.filter(name_works=name)
    print(QuerySet)
    
    return list_items


def search_precise_item(item_id: str) -> QuerySet:
    """
    Cherche un item précis par son ID.

    :param item_id:
    :return:
    """
    item = WorkList.objects.filter(id_works=item_id)

    return item


# Fonction qui sert a faire la recherche dans la page d'administration
def administration_search(query):
    # faire en sorte de passer des parametres ex: User: <username>, Ouvrage: <Nom ouvrage>
    recherche = WorkList.objects.all().filter(name_works=query)

    return recherche


def creation_id_default(librarie_id, genre, type_livre):
    copy_num = 1
    # Création de l'id
    val_id = str(
        generalIdCreationAndManagement(
            int(librarie_id), True, PermissionEnums.AA, genre, type_livre
        )
    )
    return copy_num, val_id


def create_item(response, liste_info):
    """
    Crée un item. Retourne True si l'item a été créé, False si l'item n'a pas pu être créé.

    :param response:
    :param liste_info:
    :return:
    """
    if response.method == "POST":

        for info in liste_info:
            # Vérifie que tout les éléments ont une longeur d'au moins 3.
            if (
                len(str(response.POST.get(str(info)))) < 3
                and info != "price"
                and info != "numeroCopie"
                and info != "nbrPage"
            ):
                return False  # Si il y a une erreur retourne False

        try:
            nom_livre = response.POST.get("nomLivre")
            author_name = response.POST.get("authorName")
            date_publication = response.POST.get("datePublication")
            edition_house = response.POST.get("editionHouse")
            nombre_page = response.POST.get("nbrPage")
            resume = response.POST.get("resume")
            genre = response.POST["dropdown_genre"]
            language = response.POST.get("language")

            etat = response.POST["dropdown_etat"]

            librarie_id = response.POST.get("numeroCopie")
            type_livre = response.POST["dropdown_type"]
            price = response.POST.get("price")

            # modification de la date de publication:
            date_publication = datetime.strptime(date_publication, "%Y-%m-%d")

            print(WorkList.objects.filter(name_works=nom_livre))
            print(WorkList.objects.filter(id_library=librarie_id))

            if WorkList.objects.filter(name_works=nom_livre).exists():
                print("here")
                livre_test = WorkList.objects.filter(name_works=nom_livre)

                if livre_test.filter(id_library=librarie_id).exists():
                    livres = WorkList.objects.filter(
                        name_works=nom_livre, id_library=librarie_id
                    )

                    print("ok")
                    # Prendre le livre avec le plus gros id
                    liste_id = []
                    for livre in livres:
                        liste_id.append(int(livre.id_works.split(" ")[4]))

                    copy_num = max(liste_id) + 1
                    livre_id_finale = livres[liste_id.index(copy_num - 1)].id_works

                    val_id = additionOfMultipleSameBooks(str(livre_id_finale))

                else:
                    copy_num, val_id = creation_id_default(
                        librarie_id, genre, type_livre
                    )

            else:
                copy_num, val_id = creation_id_default(librarie_id, genre, type_livre)

            # Création de l'objet
            livre = WorkList(
                id_works=val_id,
                id_library=int(librarie_id),
                name_works=str(nom_livre),
                author_name=str(author_name),
                publication_date=date_publication,
                edition_house=str(edition_house),
                length=int(nombre_page),
                resume=str(resume),
                genre=str(genre),
                language=str(language),
                state=int(etat),
                copy_number=copy_num,
                type_work=str(type_livre),
                price=decimal.Decimal(price),
            )
            livre.save()  # Enregistrement de l'objet
            print("livre créé")
            return True  # Retourne True si il le livre est créé.
        except Exception as e:
            print(f"erreur: {e}")
            return False  # Retroune False si le livre n'est pas créé."""


def delete_item(response):
    """
    Delete an item.

    :param response:
    :return:
    """
    id_delete = response.POST.get("id_work")  # Id du livre à delete

    print(id_delete, type(id_delete))
    book = WorkList.objects.filter(id_works=id_delete)[0]
    

    # Supprimer le loaned Work en premier. 
    if LoanedWorks.objects.filter(id_works=book).exists(): 
        LoanedWorks.objects.filter(id_works=book).delete()

    WorkList.objects.filter(id_works=str(id_delete)).delete()  # Delete le livre


def edit_item(response, liste_info):
    """
    Edit an item. TODO come back here to update all values of the item

    :param response:
    :param liste_info:
    :return:
    """
    item: WorkList = search_precise_item(str(response.POST.get("id_edit_livre")))[0]

    try:
        nom_livre = response.POST.get("nomLivre")
        author_name = response.POST.get("authorName")
        date_publication = response.POST.get("datePublication")
        edition_house = response.POST.get("editionHouse")
        nombre_page = response.POST.get("nbrPage")
        resume = response.POST.get("resume")
        genre = response.POST["dropdown_genre"]
        language = response.POST.get("language")

        etat = response.POST["dropdown_etat"]

        numero_copie = response.POST.get("numeroCopie")
        type_livre = response.POST["dropdown_type"]
        price = response.POST.get("price")

        # modification de la date de publication:
        date_publication = datetime.strptime(date_publication, "%Y-%m-%d")

        # Création de l'objet
        item.name_works = str(nom_livre)
        item.author_name = str(author_name)
        item.publication_date = date_publication
        item.edition_house = str(edition_house)
        item.length = int(nombre_page)
        item.resume = str(resume)
        item.genre = str(genre)
        item.language = str(language)
        item.state = int(etat)
        item.copy_number = int(numero_copie)
        item.type_work = str(type_livre)
        item.price = decimal.Decimal(price)
        item.save()
    except Exception as e:
        print(e)


def get_user(response):
    """
    Cherche l'utilisateur depuis les cookies.

    :param response: La requête.
    :return: L'utilisateur.
    """
    try:
        id_user = response.COOKIES["id_user"]
    except KeyError:
        return redirect("/")

    return UserList.objects.filter(id_users=id_user)[0]
