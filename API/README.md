# **Section - API de traitement de données** <a name="top"></a>

[Retour à l'accueil](../../../)

Ici, nous effectuons le traitement de données par API dans le but d'afficher un rendu pertinent au modèle de données importer. Afin d'effectuer cela, on utilise [**Flask**](https://flask.palletsprojects.com/).

<a href="https://flask.palletsprojects.com/">
<img width="150px" src="https://flask.palletsprojects.com/en/2.2.x/_images/flask-logo.png"/>
</a>

## Sommaire

- 1 - [Pré-requis](#1)
- 2 - [Préparation de l'environnement](#2)
- 3 - [Démarrer l'API Flask](#3)
  - 3.1 - [Démarrage principal](#3-1)
  - 3.2 - [Démarrageen mode Debug](#3-2)
- 4 - [Accès à l'API Flask](#4)

### 1 - Pré-requis - [Haut de page](#top) <a name="1"></a>

Pour pouvoir utiliser ou installer **Flask**, le dépôt dispose d'un fichier nommer **requirements.txt** constituer des dépendances essentiels à son bon fonctionnement.

De plus, selon le fichier **requirements.txt**, il est nécessaire de disposer de la version **3.10.7** de Python ou ultérieure.

### 2 - Préparation de l'environnement - [Haut de page](#top) <a name="2"></a>

**Attention**, cela s'applique pour les cas où l'environnement **venv** n'a pas été créé. Si le dossier **venv** existe déjà, les commandes ci-dessous ne sont pas nécessaires.

Que ce soit sur Windows ou MacOS, il est nécessaire :

- de vérifier que le gestionnaire de dépendances soit à jour ▶ **pip**
- de créer l'environnement ▶ **venv**
- d'activer l'environnement ▶ **activate**
- d'installer les dépendances requis ▶ **requirements.txt**

**A.1 - MacOS :**

```
python3 -m pip install --upgrade pip
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**A.2 - Windows :**

```
python -m pip install --upgrade pip
python -m venv venv
. ./venv/Scripts/activate
pip install -r requirements.txt
```

### 3 - Démarrer l'API Flask - [Haut de page](#top) <a name="3"></a>

> **Notes** : 
>
> Flask se lance en suivant les routes défini dans un fichier app.py
> 
> Les 2 premières étapes servent à configurer un projet en local, afin d'installer les dépendances que pour ce projet.
> Si vous voulez installer les dépendances en global, vous pouvez les ignorer.

#### 3.1 - Démarrage principal - [Haut de page](#top) <a name="3-1"></a>

Pour démarrer l'**API Flask**, voici la commande ci-dessous :

```
python -m flask run
```

> **NB** :
> 
> - Pensez à activer le **venv** :
>   - Mac / Linux / WSL : `source venv/bin/activate`
>   - Windows - CMD : 
>       - Par défaut : `. ./venv/Scripts/activate`
>       - Via CMD : `venv/Scripts/activate.bat`
>       - Via PS : `venv/Scripts/Activate.ps1`
> - Si vous avez besoin de quitter le venv pour retourner à une utilisation global :
> `deactivate`

#### 3.2 - Démarrage en mode Debug - [Haut de page](#top) <a name="3-2"></a>

Lancer avec le debug :

Changer dans `app.py`

> app.run(debug=True)

Éxécuter avec le debug

```
python app.py
```

### 4 - Accès à l'API Flask - [Haut de page](#top) <a name="4"></a>

- [http://127.0.0.1:5000/sample_methodes](http://127.0.0.1:5000/sample_methodes)
  - ▶ GET : test possible ✅
  - ▶ POST : test possible ✅
  - ▶ PUT : test possible ✅
  - ▶ DELETE : test possible ✅
- [http://127.0.0.1:5000/testjson](http://127.0.0.1:5000/testjson)
  - ▶ POST : test possible ✅

--------------------------------------------------------------------------------

**▶▶▶▶ A CLEAN**

### Bonus : Changer l'interpréteur pour VS Code

` Ctrl + Maj + P `

Sélectionner Python Interpreter

Sélectionner `venv/Scripts/python.exe`

Le code s'adaptera selon les modules installés dans l'environnement local

 **TODO**

---[Recherches]---

- [Flask by Example – Setting up Postgres, SQLAlchemy, and Alembic](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- [YOUTUBE - Learning Flask - Managing the database with flask-migrate and flask-sqlalchemy](https://www.youtube.com/watch?v=Ngxu0_xiZhQ)
- [Declaring Models](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/?highlight=float)
- [Session Basics](https://docs.sqlalchemy.org/en/13/orm/session_basics.html)
- [Python Try Except](https://www.w3schools.com/python/python_try_except.asp)
- [L'opérateur conditionnel ternaire en Python](https://karbotronics.com/blog/2020-03-03-python-operateur-ternaire/)