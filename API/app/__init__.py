# - - - [Importation] - - - - - - -
# Fichier Init
import pickle
from app.bdd_sqlite_manager import BddSQLiteManager
from flask import Flask


# - - - [App] - - - - - - -
# Application
app = Flask(__name__)


# - - - [BDD] - - - - - - -
# Initialisation du mananger de la BDD
bdd = BddSQLiteManager()


# - - - [Routes] - - - - - - -
# Gestion des routes
from app import routes
