# ESIEE - 2022 - IA - TP - Banque

## 1 - Sujet du projet

Prédire un accord de prêt bancaire

- Client : Fortuneo
- BDD : https://www.kaggle.com/code/mohamedadel7774/banking-dataset-with-5-different-models-techniques

## 2 - Pré-requis

- Python 3
- Jupyter-Lab

## 3 - Installation de Jupyter

### 3.1 - Préparation de l'environement

#### 3.1.1 - MacOS

```
python3 -m pip install --upgrade pip
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 3.1.2 - Windows

```
python -m pip install --upgrade pip
python -m venv venv
. ./venv/Scripts/activate
pip install -r requirements.txt
```

> Si besoin : [source de jupyter](https://jupyter.org/install)

### 3.2 - Construction de Jupyter

```
jupyter lab build
```

### 3.3 - Démarrer Jupyter

```
jupyter-lab
```

Ouvrir normalement automatique une page web : http://localhost:8888/lab.

![image](_img/001.png)

## 4 - Jupyter - Utilisation

## 4.1 - Création et utilisation d'un **Notebook**

### 4.1.2 - Qu'est-ce qu'un Notebook dans Jupyter

Un document Jupyter Notebook est un document JSON. Il suit un schéma contenant une liste ordonnée de cellules d'entrée/sortie. Celles-ci peuvent contenir du code, du texte (à l'aide de Markdown), des formules mathématiques, des graphiques et des médias interactifs. Ce document se termine généralement par l'extension ".ipynb".

[Source - wiki](https://fr.wikipedia.org/wiki/Jupyter#Jupyter_Notebook)

### 4.1.1 - Exemple de création et de lecture d'un fichier Notebook

![model_notebook](_img/002.png)

> Fichier de démo --> [**notebook_001.ipynb**](notebook_001.ipynb)

### 4.1.1 - Exemple d'exécution d'un fichier Notebook

![model_notebook](_img/003.png)

> Fichier de démo --> [**notebook_001.ipynb**](notebook_001.ipynb)

## 4.2 - Notebook disponibles

1. [**notebook_001.ipynb**](notebook_001.ipynb)
2. [**notebook_002.ipynb**](notebook_002.ipynb)