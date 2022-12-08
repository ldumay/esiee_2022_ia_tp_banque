# Import
from flask import request, jsonify
from flask_cors import CORS
import pandas as pd
from pydantic import create_model
from pycaret.regression import load_model, predict_model

# Fichier Routes
from app import app
CORS(app)

# - - - [Handle request] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

@app.post('/bank')
def predict():
    print("User request made")
    # get user data
    user_data = request.get_json()

    # Load trained Pipeline
    model = load_model("bank_model")

    # Create input/output pydantic models
    input_model = create_model("user_input", **{'age': user_data['age'], 'sex': user_data['sex'], 'children': user_data['child']})
    output_model = create_model("user_output", charges_prediction=13224.693)

    dataFrame = pd.DataFrame(input_model.dict())
    predictions = predict_model(model, data=dataFrame)
    response = jsonify({"charges_prediction": predictions["prediction_label"].iloc[0]})
    print('res', response)
    return response


# - - - [Exemple de gestion de méthodes] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Exemple de gestion de méthodes
@app.route('/sample_methodes', methods=['GET', 'POST', 'PUT', 'DELETE'])
def sample_methodes():
    if request.method=='GET':
        return "Cette méthode est un GET 😉👌"
    elif request.method=='POST':
        return " Cette méthode est un POST 😉👌"
    elif request.method=='PUT':
        return " Cette méthode est un PUT 😉👌"
    elif request.method=='DELETE':
        return " Cette méthode est un DELETE 😉👌"
    else:
        return "Je ne sais pas quoi faire avec ta requète 🤷‍♂️"
