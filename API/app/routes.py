# Fichier Routes
from app import app
from flask import request, redirect
import jsonpickle
import numpy as np
from werkzeug.debug import console


# - - - [Test] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

@app.route('/testjson', methods=['POST'])
def home():
    data = request.get_json()
    # listData = list(data)
    if data:
        for d in data:
            print(d["heure"], flush=True)

    return jsonpickle.encode(data)


# - - - [Exemple de gestion de méthodes] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Exemple de gestion de méthodes
@app.route('/sample_methodes', methods=['GET', 'POST', 'PUT', 'DELETE'])
def sample_methodes():
    if request.method=='GET':
        return "Cette méthode est un GET 😉👌"
    elif request.method=='POST':
        return " Cette méthode est un GET 😉👌"
    elif request.method=='PUT':
        return " Cette méthode est un PUT 😉👌"
    elif request.method=='DELETE':
        return " Cette méthode est un DELETE 😉👌"
    else:
        return "Je ne sais pas quoi faire avec ta requète 🤷‍♂️"
