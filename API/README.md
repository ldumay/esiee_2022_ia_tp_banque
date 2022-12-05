# **Section - API** <a name="top"></a>

[Retour à l'accueil](../../../)

## Backend - App API - Flask Python

### 1 - Pré-requis :

- Python : **v3.10.7**

### 2 - Initialiser et récupérer les dépendances d'un projet python

🚨 C'est la première fois que je fais un projet python, si jamais une commande ne fonctionne pas, n'hésitez pas à corriger le document

Flask se lance en suivant les routes défini dans un fichier app.py

Les 2 premières étapes servent à configurer un projet en local, afin d'installer les dépendances que pour ce projet.
Si vous voulez installer les dépendances en global, vous pouvez les ignorer

## Déplacer dans le dossier

```
cd backend
```

#### 2.1 - Créer un environnement local 

```
python -m venv venv
```

#### 2.2 - Utiliser la console lié à l'environnement local

Docs : https://docs.python.org/3/library/venv.html

- Mac / Linux / WSL : 

```
source venv/bin/activate
```

- Windows - CMD : 

```
Par défaut :
. ./venv/Scripts/activate

Via CMD :
venv/Scripts/activate.bat

Via PS : 
venv/Scripts/Activate.ps1
```

### Bonus : Changer l'interpréteur pour VS Code

` Ctrl + Maj + P `

Sélectionner Python Interpreter

Sélectionner `venv/Scripts/python.exe`

Le code s'adaptera selon les modules installés dans l'environnement local

#### 2.3 - Installer toutes les dépendances lié au projet 

```
python -m pip install -r requirements.txt
```

> **Si besoin de mettre à jour de fichier `requirements.txt`** :
> 
> ```
> python -m pip freeze > requirements.txt
> ```

#### 2.4 - Sortir du venv

Si vous avez besoin de quitter le venv pour retourner à une utilisation global

> `deactivate`

### 3 - Accès à API

#### 3.1 - Lancer l'application backend python avec flask

```
python -m flask run
```
---

Lancer avec le debug :

Changer dans `app.py`

> app.run(debug=True)

Éxécuter avec le debug

```
python app.py
```
 ### 3.2 Point d'accès de l'API

 **TODO**

---[Recherches]---

- [Flask by Example – Setting up Postgres, SQLAlchemy, and Alembic](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- [YOUTUBE - Learning Flask - Managing the database with flask-migrate and flask-sqlalchemy](https://www.youtube.com/watch?v=Ngxu0_xiZhQ)
- [Declaring Models](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/?highlight=float)
- [Session Basics](https://docs.sqlalchemy.org/en/13/orm/session_basics.html)
- [Python Try Except](https://www.w3schools.com/python/python_try_except.asp)
- [L'opérateur conditionnel ternaire en Python](https://karbotronics.com/blog/2020-03-03-python-operateur-ternaire/)