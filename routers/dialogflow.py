from flask import Blueprint, request
import json

dialogflow_blueprint = Blueprint(
    "dialogflow",
    __name__,
)

with open('datasets/glossary.json') as file:
    data = json.load(file)


@dialogflow_blueprint.route("/dialogflow", methods=['POST'])
def get_response():
    req = request.get_json(force=True)
    queryResult = req.get('queryResult')
    parameters = queryResult.get("parameters")
    glossary: str = parameters.get('glossary')

    response: str = ""
    for intent in data['intents']:
        if intent['tagKH'] == glossary:
            response = intent['response']

    return {
        "fulfillmentText":  response if response else "សូមទោសផង ប្អូននៅមិនទាន់យល់ពីសំណួរនេះ ប្អូននឹងយកទៅសិក្សាបន្ថែម"
    }
