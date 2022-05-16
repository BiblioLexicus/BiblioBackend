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
* [Usage](#Usages)
* [Améliorations possibles](#amliorations-possibles)

### Captures d'écran

![page accueil](https://github.com/BiblioLexicus/BiblioBackend/blob/assets/assets/frontPageBiblioLexicus.png)
![page administration](https://github.com/BiblioLexicus/BiblioBackend/blob/assets/assets/AdministrationPageBiblioLexicus.png)
![page de résultats recherchés](https://github.com/BiblioLexicus/BiblioBackend/blob/assets/assets/ResultsPage.png)
![page d'un livre](https://github.com/BiblioLexicus/BiblioBackend/blob/assets/assets/BookPageBiblioLexicus.png)
![page d'inscription](https://github.com/BiblioLexicus/BiblioBackend/blob/assets/assets/signupPageBiblioLexicus.png)
![page d'enregistrement](https://github.com/BiblioLexicus/BiblioBackend/blob/assets/assets/LoginPageBiblioLexicus.png)

### Technologies(fr)

Technologies utilisées :

* Django version: 4.0.4
* SQL and MariaDB: oldest version 10.4

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

#### Créer une base de données

> Pour le moment, utiliser le fichier sql fourni (dbconfig/MtlBiblioDb_V1-5.sql) pour créer une base de données et spécifier que vous utilisez cette
> base de données dans le .env

La base de données doit supporter InnoDB en tant que moteur de stockage.

#### Configuration et lancement du serveur

Après avoir installé toutes les dépendances avec poetry, rentrez dans environment avec `poetry shell`

Il est nécessaire de configurer quelques paramètres. 

Un script de configuration est disponible en faisant `python setup.py --deploy/debug`

Pour une utilisation de test ou de développement, spécifiez `--debug`

Pour une utilisation de déploiement, spécifiez `--deploy`. 
**NOTE : Ce projet n'a pas été testé dans des situations réelles et le système d'authentification n'est pas au point. 
Il n'est donc PAS recommandé d'utiliser ce projet en tant que solution complète en ce moment. Si ce projet est utilisé dans pareille 
situation, les auteurs du projet ne sont PAS responsables des conséquences possibles.**

Pour démarrer l'application, lancer en utilisant poetry
``` python Backend/manage.py runserver```

### Usages

Stockage, recherche et archivage de livre stockés dans une multitude de bibliothèques

Une fois le site web démarré, créer un utilisateur et s'authentifier. Pour pouvoir créer et supprimer des livres, il est
nécessaire d'avoir la permission administrateur.
Pour ce faire, créer un super-utilisateur : `python3 Backend/manage.py createsuperuser` et changer les permissions de
l'utilisateur admin dans la page /admin
L'admin peut créer une bibliothèque et des livres, l'user peut uniquement rechercher et emprunter des livres

### Améliorations Possibles

- Ajout d'une fonctionalité d'ajout d'image de profil pour les utilisateurs. Le fichier SQL reflète cette fonctionalité,
  il faut seulement implanter le tout
- Ajout d'une fonctionalité d'ajout d'image de livre par les utilisateurs autre que l'image de défaut
- Tests et optimisations à plus grande échelle
- Simplification du processus de setup pour setup le projet sur un autre ordinateur
- Ajout de fonction de recherche de type brouillées (fuzzy search) grâce à l'algorithme de "double metaphone", comme
  illustré dans le repository suivant : https://github.com/AtomBoy/double-metaphone
- Meilleure gestion de la création d'administrateurs et des permissions (éviter d'avoir à passer par la page /admin)

## English

## Public Library Mockup Project Backend

Backend of the BiblioLexicus project.

### Table of content

* [Screenshots](#captures-dcran)
* [Technologies](#Technology)
* [Setting Up](#Setting-up)
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

#### Database configuration

Install any new dependency with `poetry add <package>`
> For the time being, create a mysql database using the config (dbconfig/MtlBiblioDb_V1-5.sql) file and specify its name in a .env file

La base de données doit supporter InnoDB en tant que moteur de stockage.

#### Configuration and start of server

After installing the dependencies with Poetry, enter the new environment with `poetry shell`

It is necessary to configure some project parameters.

A configuration script is available with `python setup.py --deploy/debug`

For a test or development use case, specify `--debug`

For a deployment, specify `--deploy`. 
**NOTE: This project has not been tested in real situations and the authentication system is not on point. 
It is then NOT recommended using this project as a complete solution at this point. If the project is used in that kind
of situation, the project authors are NOT responsible for the possible consequences.**

Finally, to start the application,
``` python Backend/manage.py runserver```

### Use Cases

Storage and search of books, movies and video-games in a library-like environment
To use the website, create a user and authenticate. You will need a use with admin permissions to be able to create and
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
