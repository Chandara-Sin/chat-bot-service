import json
from google.cloud import dialogflow
import os

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
            if taxpayer in data['tagKH'] and 'registered' not in data['intent']:
                response = data['responses'][0]
    return response


def get_taxpayer_registered(taxpayer: str):
    response: str = ""
    for data in taxpayer_data:
        if (data['tagKH']):
            if taxpayer in data['tagKH'] and 'registered' in data['intent']:
                response = data['responses'][0]
    return response


def create_intent(display_name, training_phrases_parts, message_texts: str):
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(
        os.getenv("DIALOGFLOW_PROJECT_ID", ""))
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(
            text=training_phrases_part)

        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=[message_texts])
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[
            message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))
