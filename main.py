from flask import Flask, request, jsonify
from flask_cors import CORS
from routers import user
import json

app = Flask(__name__)
CORS(app)


app.register_blueprint(user.account_blueprint, url_prefix="/api/v1")


@app.route("/api/v1/healthz")
def health():
    return jsonify({"message": "Ok v1"}), 200


with open('glossary.json') as file:
    data = json.load(file)


@app.route("/api/v1/gdt", methods=['POST'])
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


if __name__ == "__main__":
    app.run(debug=True)
