import requests
import json
from dotenv import load_dotenv
import os

def envoyer_message_webhook(url_webhook, message):
    data = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url_webhook, data=json.dumps(data), headers=headers)
    if response.status_code == 204:
        print("Message envoyé avec succès au webhook.")
    else:
        print(f"Échec de l'envoi du message. Code d'état HTTP : {response.status_code}")

# URL du webhook Discord
load_dotenv('((environement.env))')
url_webhook = os.environ['DISCORD']
envoyer_message_webhook(url_webhook, 'Message')