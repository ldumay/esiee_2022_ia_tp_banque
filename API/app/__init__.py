# Fichier Init
from flask import Flask

# Application
app = Flask(__name__)

# Gestion des routes
from app import routes
