# **Section - Recherche de données** <a name="top"></a>

[Retour à l'accueil](../../../)

Ici, nous effectuons des recherches de données dans le but de trouver un modèle de données pertinent selon le type de données reçu et la cible de sortie. Afin d'effectuer cela, on utilise [**Jupyter - Lab**](https://jupyter.org/).

<a href="https://jupyter.org/">
<img width="100px" src="https://jupyter.org/assets/homepage/main-logo.svg"/>
</a>

## Sommaire

- 1 - [Pré-requis](#1)
- 2 - [Jupyter](#2)
  - 2.1 - [Installation de Jupyter](#2-1)
    - 2.1.1 - [Préparation de l'environnement](#2-1-1)
    - 2.1.2 - [ Démarrer Jupyter](#2-1-2)
  - 2.2 - [Utilisation de Jupyter](#2-2)
    - 2.2.1 - [Qu'est-ce qu'un Notebook dans Jupyter](#2-2-1)
    - 2.2.2 - [Exemple de création et de lecture d'un fichier Notebook](#2-2-2)
    - 2.2.3 - [Exemple d'exécution d'un fichier Notebook](#2-2-3)
- 3 - [Travaux pratiques](#3)
  - 3.1 - [TP - Titanic](#3-1)
  - 3.2 - [TP - Banque](#3-2)
    - 3.2.1 - [Sujet du projet](#3-2-1)

## 1 - Pré-requis - [Haut de page](#top) <a name="1"></a>

Pour pouvoir utiliser ou installer **Jupyter - Lab**, le dépôt dispose d'un fichier nommer **requirements.txt** constituer des dépendances essentiels à son bon fonctionnement.

De plus, selon le fichier **requirements.txt**, il est nécessaire de disposer d'un version de Python comprise entre **>=3.7** - **<3.11**.

## 2 - Jupyter - [Haut de page](#top) <a name="2"></a>

### 2.1 - Installation de Jupyter - [Haut de page](#top) <a name="2-1"></a>

#### 2.1.1 - Préparation de l'environnement - [Haut de page](#top) <a name="2-1-1"></a>

**Attention**, cela s'applique pour les cas où l'environnement **venv** n'a pas été créé. Si le dossier **venv** existe déjà, les commandes ci-dessous ne sont pas nécessaires.

Que ce soit sur Windows ou MacOS, il est nécessaire :

- de vérifier que le gestionnaire de dépendances soit à jour ▶ **pip**
- de créer l'environnement ▶ **venv**
- d'activer l'environnement ▶ **activate**
- d'installer les dépendances requis ▶ **requirements.txt**

**A.1 - Installation sur MacOS :**

```
python3 -m pip install --upgrade pip
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**A.2 - Installation sur Windows :**

```
python -m pip install --upgrade pip
python -m venv venv
. ./venv/Scripts/activate
pip install -r requirements.txt
```

> Si besoin : [source de jupyter](https://jupyter.org/install)

**B - Construction de Jupyter :**

Avant de pouvoir utiliser le **Jupyter - Lab**, il est nécessaire de construire le construire si ce n'est pas le cas.

```
jupyter lab build
```

#### 2.1.2 -  Démarrer Jupyter - [Haut de page](#top) <a name="2-1-2"></a>

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

Ouvrir normalement automatique une page web : http://localhost:8888/lab.

![image](_img/001.png)

### 2.2 - Utilisation de Jupyter - [Haut de page](#top) <a name="2-2"></a>

#### 2.2.1 - Qu'est-ce qu'un Notebook dans Jupyter - [Haut de page](#top) <a name="2-2-1"></a>

Un document Jupyter Notebook est un document JSON. Il suit un schéma contenant une liste ordonnée de cellules d'entrée/sortie. Celles-ci peuvent contenir du code, du texte (à l'aide de Markdown), des formules mathématiques, des graphiques et des médias interactifs. Ce document se termine généralement par l'extension ".ipynb".

[Source - wiki](https://fr.wikipedia.org/wiki/Jupyter#Jupyter_Notebook)

#### 2.2.2 - Exemple de création et de lecture d'un fichier Notebook - [Haut de page](#top) <a name="2-2-2"></a>

![model_notebook](_img/002.png)

#### 2.2.3 - Exemple d'exécution d'un fichier Notebook - [Haut de page](#top) <a name="2-2-3"></a>

![model_notebook](_img/003.png)

## 3 - Travaux pratiques - [Haut de page](#top) <a name="3"></a>

### 3.1 - TP - Titanic - [Haut de page](#top) <a name="3-1"></a>

Exemple d'étude de données réaliser en cours.

- Fichiers dispnobiles : 
  - [model_titanic.ipynb](model_titanic.ipynb)
  - [model_titanic.html](model_titanic.html)
  - /datas/
    - [titanic/gender_submission.csv](/datas/titanic/gender_submission.csv)
    - [titanic/test.csv](/datas/titanic/test.csv)
    - [titanic/train.csv](/datas/titanic/train.csv)
  
### 3.2 - TP - Banque - [Haut de page](#top) <a name="3-2"></a>

#### 3.2.1 - Sujet du projet - [Haut de page](#top) <a name="3-2-1"></a>

Prédire un accord de prêt bancaire

- Client : Fortuneo
- BDD : https://www.kaggle.com/code/mohamedadel7774/banking-dataset-with-5-different-models-techniques

- Fichiers dispnobiles : 
  - [notebook_Zchen.ipynb](notebook_Zchen.ipynb)
  - /datas/
    - [bank/bank-full.csv](/datas/bank/bank-full.csv)
    - [bank/bank-full-col-definition.txt](/datas/bank/bank-full-col-definition.txt)