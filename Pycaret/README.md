# **Section - PyCaret avec Jupyter** <a name="top"></a>

[Retour à l'accueil](../../../)

Ici, nous effectuons un test de PyCaret avec Jupyter.

<a href="https://pycaret.org/">
<img width="150px" src="https://pycaret.org/wp-content/uploads/2022/01/Transparent_file1-01-01-01-01.png"/>
</a>

## Sommaire

- 1 - [Pré-requis](#1)
- 2 - [Préparation de l'environnement](#2)
- 3 - [Démarrer Jupyter](#3)
- 4 - [Sources](#4)

### 1 - Pré-requis - [Haut de page](#top) <a name="1"></a>

Pour pouvoir utiliser ou installer **Flask**, le dépôt dispose d'un fichier nommer **requirements.txt** constituer des dépendances essentiels à son bon fonctionnement.

De plus, selon le fichier **requirements.txt**, il est nécessaire de disposer de la version **3.10** de Python ou ultérieure.

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

**B - Construction de Jupyter :**

Avant de pouvoir utiliser le **Jupyter - Lab**, il est nécessaire de construire le construire si ce n'est pas le cas.

```
jupyter lab build
```

### 3 - Démarrer Jupyter - [Haut de page](#top) <a name="3"></a>

Pour démarrer le **Jupyter - Lab**, voici la commande ci-dessous :

```
jupyter-lab
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

### 4 - Sources - [Haut de page](#top) <a name="4"></a>

- Sources :
  - [https://pycaret.org/](https://pycaret.org/)
  - [https://pycaret.gitbook.io/docs/get-started/installation](https://pycaret.gitbook.io/docs/get-started/installation)