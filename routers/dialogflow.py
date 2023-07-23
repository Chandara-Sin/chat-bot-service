from flask import Blueprint, request
from domain.dialogflow import get_glossary, get_taxpayer, get_taxpayer_registered

dialogflow_blueprint = Blueprint(
    "dialogflow",
    __name__,
)


@dialogflow_blueprint.route("/dialogflow", methods=['POST'])
def get_response():
    req = request.get_json(force=True)
    queryResult = req.get('queryResult')
    action = queryResult.get("action")
    parameters = queryResult.get("parameters")
    glossary: str = parameters.get('glossary')
    taxpayer: str = parameters.get("taxpayer")

    response: str = ""

    if (action == 'input.glossary'):
        response = get_glossary(glossary)
    elif (action == 'input.taxpayer'):
        response = get_taxpayer(taxpayer)
    elif (action == 'input.taxpayer_registered'):
        response = get_taxpayer_registered(taxpayer)

    return {
        "fulfillmentText":  response if response else "សូមទោសផង ប្អូននៅមិនទាន់យល់ពីសំណួរនេះ ប្អូននឹងយកទៅសិក្សាបន្ថែម"
    }
