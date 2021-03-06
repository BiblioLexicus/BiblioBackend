import decimal
import random
from datetime import date, datetime

from dateutil.relativedelta import relativedelta
from django.db.models.query import QuerySet
from django.shortcuts import redirect
from fast_autocomplete import AutoComplete

from .IDEnums import PermissionEnums
from .IDManagement import additionOfMultipleSameBooks, generalIdCreationAndManagement
from .models import Comments, LoanedWorks, UserList, WorkList, WorkMediaList


def resultats_possibles(recherche):
    all_works_name = {works.name_works: {} for works in WorkList.objects.all()}

    autocomplete = AutoComplete(words=all_works_name)
    all_matched_works = autocomplete.search(word=str(recherche), max_cost=3, size=10)

    return all_matched_works


def voir_commentaire(item_id):
    """
    Affiche les commentaires sur la page d'un item

    :param item_id: ID de l'item pour lequel nous voulons avoir les commentaires
    :type item_id: int

    :returns: une liste contenant des objets de commentaires
    :rtype: list
    """
    try:
        livre = WorkList.objects.filter(id_works=str(item_id))[0]
        list_commentaires = Comments.objects.filter(id_works=livre)
        return list_commentaires

    except Exception:
        return []


def ajouter_commentaire(response):
    """
    Ajouter un commentaire

    :param response: Requete DJANGO
    :type response: requete POST

    :returns: Retourne rien si le livre est créé et retourne False si il y a une erreur
    :rtype: bool
    """
    if len(str(response.POST.get("ecritureComm"))) > 1:
        try:
            user_id = response.COOKIES["id_user"]

            new_comm = Comments(
                id_comments=int(
                    int(user_id.split(" ")[0]) + random.randrange(0, 2147483646)
                ),
                id_works=WorkList.objects.filter(id_works=response.POST.get("id_work"))[
                    0
                ],
                id_users=UserList.objects.filter(id_users=str(user_id))[0],
                release_date=date.today(),
                comment_text=str(response.POST.get("ecritureComm")),
            )
            new_comm.save()
        except Exception:
            return False


def emprunter(response):
    """
    Emprunter un item.

    :param response: Requete Django
    :type response: Requete POST

    :return: True si l'objet est emprunter; False si l'objet n'est pas emprunté
    :rtype: bool
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

    :param user_id: ID de l'utilisateur
    :type user_id: str

    :return: liste de livre emprunté
    :rtype: list
    """
    user = UserList.objects.filter(id_users=str(user_id))[0]
    liste_emprunts = LoanedWorks.objects.filter(id_users=user)

    liste_final = []

    for livre in liste_emprunts:
        # Permet de prendre le livre dans le loaned works et non le loaned works.
        liste_final.append(livre.id_works)

    return liste_final


def search_home(response):
    """
    recherche dans la page d'Accueil

    :param response: requete Django
    :return: empty str
    """
    if response.method == "GET":
        if response.GET.get("search"):
            recherche = response.GET.get("livre")
            return recherche  # return la valeur recherchée
    return ""


def search_item_by_name(name: str) -> QuerySet:
    """
    Cherche l'item avec son nom

    :param name: Nom du livre recherché
    :return: liste de livres trouvés à l'aide du nom
    """
    list_items: QuerySet = WorkList.objects.all().filter(name_works=name)

    return list_items


def search_precise_item(item_id: str) -> QuerySet:
    """
    Cherche un item précis par son ID.

    :param item_id: ID du livre recherché
    :return: liste de livres trouvé à l'aide de l'ID
    """
    item = WorkList.objects.all().filter(id_works=item_id)

    return item


def administration_search(query):
    """
    Recherche dans la page d'administration

    :param query: Nom du livre recherché
    :return: liste de livres trouvé à l'aide de la query
    """
    # faire en sorte de passer des parametres ex: User: <username>, Ouvrage: <Nom ouvrage>
    recherche = WorkList.objects.all().filter(name_works=query)

    return recherche


def creation_id_default(librarie_id, genre, type_livre):
    """
    Creation de l'ID de livre par défaut

    :param librarie_id: ID de la librairie
    :param genre: genre du livre
    :param type_livre: type du livre

    :returns: Retourne numero de copie du livre ainsi que son ID.
    """
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

    :param response: requete Django
    :param liste_info: liste d'information sur le livre
    :return: True si livre est créé, False si erreur
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
            edition_house = response.POST.get("editionr les nuls','House")
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

            if WorkList.objects.filter(name_works=nom_livre).exists():

                livre_test = WorkList.objects.filter(name_works=nom_livre)

                if livre_test.filter(id_library=librarie_id).exists():
                    if livre_test.filter(author_name=author_name).exists():
                        livres = WorkList.objects.filter(
                            name_works=nom_livre,
                            id_library=librarie_id,
                            author_name=author_name,
                        )

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

            if response.POST.get("work_media") == "":
                img_path = "https://raw.githubusercontent.com/BiblioLexicus/Design/main/Book_image_not_found.jpg"
            else:
                img_path = str(response.POST.get("work_media"))
            w = WorkMediaList(id_works=livre, photo_path_work=img_path)
            w.save()
            print("livre créé")
            return True  # Retourne True si il le livre est créé.
        except Exception as e:
            print(f"erreur: {e}")
            return False  # Retroune False si le livre n'est pas créé."""


def delete_item(response):
    """
    Delete un item.

    :param response: requete Django
    :return: None
    """
    id_delete = response.POST.get("id_work")  # Id du livre à delete

    print(id_delete, type(id_delete))
    book = WorkList.objects.filter(id_works=id_delete)[0]

    # Supprimer le loaned Work en premier.
    if LoanedWorks.objects.filter(id_works=book).exists():
        LoanedWorks.objects.filter(id_works=book).delete()

    if Comments.objects.filter(id_works=book).exists():
        liste_commentaires = Comments.objects.filter(id_works=book)
        for commentaire in liste_commentaires:
            commentaire.delete()

    work_media = WorkMediaList.objects.filter(id_works=book)[0]
    work_media.delete()

    WorkList.objects.filter(id_works=str(id_delete)).delete()  # Delete le livre


def edit_item(response, liste_info):
    """
    Edit an item. TODO come back here to update all values of the item

    :param response: requete Django
    :param liste_info: liste d'information du livre
    :return: None
    """
    # Ici "id_edit_livre" et non "id_edit"
    item: WorkList = search_precise_item(response.POST.get("id_edit_livre"))[0]
    work_media = WorkMediaList.objects.filter(id_works=item)[0]

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

        librairie = response.POST.get("numeroCopie")
        type_livre = response.POST["dropdown_type"]
        price = response.POST.get("price")

        # modification de la date de publication:
        date_publication = datetime.strptime(date_publication, "%Y-%m-%d")

        # Création de l'objet
        item.name_works = str(nom_livre)
        item.id_library = int(librairie)
        item.author_name = str(author_name)
        item.publication_date = date_publication
        item.edition_house = str(edition_house)
        item.length = int(nombre_page)
        item.resume = str(resume)
        item.genre = str(genre)
        item.language = str(language)
        item.state = int(etat)
        item.type_work = str(type_livre)
        item.price = decimal.Decimal(price)
        item.save()

        if response.POST.get("work_media") == "":
            img_path = "https://raw.githubusercontent.com/BiblioLexicus/Design/main/Book_image_not_found.jpg"
        else:
            img_path = str(response.POST.get("work_media"))

        work_media.photo_path_work = img_path
        work_media.save()
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
