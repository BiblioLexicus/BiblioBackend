# BiblioBackend - Simulation du système d'archivage et de prêt d'une bibliothèque publique (FR)
Simulation d'un système de gestion de livres en bibliothèque. 
## Table de contenu

* [Capture d'écran](#capture-dcran)
* [Technologies](#technologies(fr))
* [Instruction d'installation](#instruction-dinstallation)
* [Usage](#usage)
* [Améliorations possibles](#amliorations-possibles)


## Capture d'écran
![page accueil](https://github.com/BiblioLexicus/BiblioBackend/blob/assets/assets/frontPageBiblioLexicus.png)


## Technologies(fr)
Used technologies in this project
* Django version: 4.0.4
* SQL and MariaDB: oldest version 10.3

## Instruction d'installation

Install dependencies with `poetry install` (`pip install poetry`)

Install hooks:
```
poetry run pre-commit install -t=pre-commit -t=pre-push
```

Install any new dependancy with `poetry add <package>`

## Usages



## Améliorations Possibles




# BiblioBackend - Public Library Mockup Project Backend (EN)
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
