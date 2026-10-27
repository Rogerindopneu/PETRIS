import requests
from config.settings import settings

headers = {
    "Content-Type": "application/json",
    "apikey": settings.EVOLUTION_API_KEY
}

def send_text_message(number: str, text: str):
    url = f"{settings.EVOLUTION_API_URL}/message/sendText/{settings.EVOLUTION_INSTANCE_NAME}"
    payload = {
        "number": number,
        "options": {"delay": 1200, "presence": "composing"},
        "textMessage": {"text": text}
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def send_presence(number: str):
    url = f"{settings.EVOLUTION_API_URL}/chat/sendPresence/{settings.EVOLUTION_INSTANCE_NAME}"
    payload = {"number": number, "delay": 1200, "presence": "composing"}
    requests.post(url, json=payload, headers=headers)