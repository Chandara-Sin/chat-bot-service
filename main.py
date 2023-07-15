from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open('glossary.json') as file:
    data = json.load(file)


@app.route("/api/v1/healthz")
def health():
    return jsonify({"message": "Ok v1"}), 200


@app.route("/api/v1/users/<id>")
def get_user(id):
    req_name = request.args.get("name")
    user = {
        "id": id,
        "name": req_name if req_name else "Chandara",
        "email": "name@example.com"
    }
    return jsonify(user), 200


@app.route("/api/v1/users", methods=['POST'])
def create_user():
    req_user = request.get_json()
    return jsonify(req_user), 201


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
