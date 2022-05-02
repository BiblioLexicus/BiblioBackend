# BiblioBackend

* [Français](#franais)
* [English](#english)

## Français

## Simulation du système d'archivage et de prêt d'une bibliothèque publique

Simulation d'un système de gestion de livres en bibliothèque.

### Table de contenu

* [Capture d'écran](#captures-dcran)
* [Technologies](#technologies(fr))
* [Instruction d'installation](#instruction-dinstallation)
* [Usage](#usage)
* [Améliorations possibles](#amliorations-possibles)

### Captures d'écran

![page accueil](https://github.com/BiblioLexicus/BiblioBackend/blob/assets/assets/frontPageBiblioLexicus.png)
![page administration](https://github.com/BiblioLexicus/BiblioBackend/blob/assets/assets/AdministrationPageBiblioLexicus.png)
![page de resultats recherche](https://github.com/BiblioLexicus/BiblioBackend/blob/assets/assets/ResultsPage.png)
![page d'un livre](https://github.com/BiblioLexicus/BiblioBackend/blob/assets/assets/BookPageBiblioLexicus.png)
![page d'inscription](https://github.com/BiblioLexicus/BiblioBackend/blob/assets/assets/signupPageBiblioLexicus.png)
![page d'enregistrement](https://github.com/BiblioLexicus/BiblioBackend/blob/assets/assets/LoginPageBiblioLexicus.png)

### Technologies(fr)

Technologies utilisés:

* Django version: 4.0.4
* SQL and MariaDB: oldest version 10.3

### Instruction d'installation

Installer les dépendances avec `poetry install`

- Si nécessaire, installer Poetry avec bash:

```
curl -sSL https://install.python-poetry.org | python3 -
```

- Si nécessaire, installer Poetry avec Powershell:

```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

- Crochets d'installation:

```
poetry run pre-commit install -t=pre-commit -t=pre-push
```

Installer toute nouvelle dépendance avec `poetry add <package>`

> Pour le moment, utiliser le fichier sql fourni pour créer une base de données et spécifier que vous utilisez cette
> base de données dans le .env

pour démarrer l'application, lancer en utilisant poetry
``` python backend/manage.py runserver```

### Usages

Stockage, recherche et archivage de livre stockés dans une multitude de bibliothèques

Une fois le site web démarré, créer un utilisateur et s'authentifier. Pour pouvoir créer et supprimer des livres, il est
nécessaire d'avoir la permission administrateur.
Pour se faire, créer un super user: `python3 Backend/manage.py createsuperuser` et changer les permissions de
l'utilisateur admin dans la page /admin
L'admin peut créer une bibliothèque et des livres, l'user peut uniquement rechercher et emprunter des livres

### Améliorations Possibles

- ajout d'une fonctionalité d'ajout d'image de profil pour les utilisateurs. Le fichier SQL reflète cette fonctionalité,
  il faut seulement implanter le tout
- ajout d'une fonctionalité d'ajout d'image de livre par les utilisateurs autre que l'image de défaut
- tests et optimisations à plus grande échelle
- simplification du processus de setup pour setup le projet sur un autre ordinateur
- ajout de fonction de recherche de type brouillées (fuzzy search) grâce à l'algorithme de "double metaphone", comme
  illustré dans le repository suivant: https://github.com/AtomBoy/double-metaphone
- meilleur gestion de la création d'administateurs et des permissions (éviter d'avoir a passer par la page /admin)

## English

## Public Library Mockup Project Backend

Backend of the BiblioLexicus project.

### Table of content

* [Screenshots](#captures-dcran)
* [Technologies](#Technologies)
* [Setting Up](#Setting-Up)
* [Use cases](#use-cases)
* [Possible improvements](#possible-improvements)

### Technology

Used technologies in this project

* Django version: 4.0.4
* SQL and MariaDB: minimal version: 10.3

### Setting up

Install dependencies with `poetry install`

- Install poetry with bash:

```
curl -sSL https://install.python-poetry.org | python3 -
```

- Install poetry with Powershell:

```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

- Install hooks:

```
poetry run pre-commit install -t=pre-commit -t=pre-push
```

Install any new dependancy with `poetry add <package>`
> for the time being, create a mysql library using the config file and specify its name in a .env file

Start the webpage:

```
poetry shell
python3 Backend/manage.py runserver
```

### Use Cases

Storage and search of books, movies and video-games in a library-like environment
To use the web site, create a user and authenticate. You will need a use with admin permissions to be able to create and
delete books and libraries. To get it, create a superuser with:`python3 Backend/manage.py createsuperuser`
Then, change the permission of the user to admin in the /admin page. A normal user can only browse the database and
borrow books.

### Possible Improvements

- Add the option to set a profile picture by users
- Add the possibility to set a picture of a book
- test and optimise the project on a larger scale (10 000 + works)
- Simplify and mainstream the setup process
- Add fuzzy search with the double metaphone algorithm. ex: <https://github.com/AtomBoy/double-metaphone>
- Improve the permission system in place, lock everyone out of the /admin page
