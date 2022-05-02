# BiblioBackend

* [Français](#franais)
* [English](#english)

## Français
## Simulation du système d'archivage et de prêt d'une bibliothèque publique
Simulation d'un système de gestion de livres en bibliothèque. 
### Table de contenu

* [Capture d'écran](#capture-dcran)
* [Technologies](#technologies(fr))
* [Instruction d'installation](#instruction-dinstallation)
* [Usage](#usage)
* [Améliorations possibles](#amliorations-possibles)


### Capture d'écran
![page accueil](https://github.com/BiblioLexicus/BiblioBackend/blob/assets/assets/frontPageBiblioLexicus.png)
![page administration](https://github.com/BiblioLexicus/BiblioBackend/blob/assets/assets/AdministrationPageBiblioLexicus.png)
![page de résultats recherche](https://github.com/BiblioLexicus/BiblioBackend/blob/assets/assets/ResultsPage.png)
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

Pour le moment, utiliser le fichier sql fourni pour créer une base de données et spécifier que vous utilisez cette base de données dans le .env

pour démarrer l'application, lancer en utilisant poetry 
``` python backend/```

### Usages



### Améliorations Possibles

- ajout d'une fonctionalité d'ajout d'image de profil pour les utilisateurs. Le fichier SQL reflète cette fonctionalité, il faut seulement implanter le tout
- ajout d'une fonctionalité d'ajout d'image de livre par les utilisateurs autre que l'image de défault
- tests et optimisations à plus grande échelle
- simplification du processus de setup pour setup le projet sur un autre ordinateur

## English
## Public Library Mockup Project Backend (EN)
Backend of the BiblioLexicus project.

## Table of content

* []()
* [Technologies](#Technologies)
* [Setting Up](#Setting-Up)

## Technology
Used technologies in this project
* Django version: 4.0.4
* SQL and MariaDB: minimal version: 10.3

## Setting up

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
