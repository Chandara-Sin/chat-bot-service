from flask import Blueprint, request
from domain.dialogflow import get_glossary, get_taxpayer, get_taxpayer_registered, create_intent

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
        "fulfillmentText":  response if response else "សូមទោសផង ខាងនាងខ្ញុំនៅមិនទាន់យល់ពីសំណួរនេះ ខាងនាងខ្ញុំនឹងយកទៅសិក្សាបន្ថែម"
    }, 201


@dialogflow_blueprint.route("/dialogflow/intent", methods=['POST'])
def dialogflow_intent():
    req = request.get_json(force=True)
    display_name = req["display_name"]
    training_phrases_parts = req["training_phrases_parts"]
    message_texts = req["message_texts"]

    res = create_intent(display_name, training_phrases_parts, message_texts)

    return {"message": f"Intent '{display_name}' created successfully.", "data": res}, 201
