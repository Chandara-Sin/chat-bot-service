import json

with open('datasets/glossary.json') as file:
    glossary_data = json.load(file)

with open('datasets/taxpayer.json') as file:
    taxpayer_data = json.load(file)


def get_glossary(glossary: str):
    response: str = ""
    for intent in glossary_data['intents']:
        if intent['tagKH'] == glossary:
            response = intent['response']
    return response


def get_taxpayer(taxpayer: str):
    response: str = ""
    for data in taxpayer_data:
        if (data['tagKH']):
            if taxpayer in data['tagKH']:
                response = data['responses'][0]
    return response
