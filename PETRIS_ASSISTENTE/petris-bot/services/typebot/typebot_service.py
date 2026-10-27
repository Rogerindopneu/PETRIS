import requests
from config.settings import settings

headers = {
    "Content-Type": "application/json"
}

def start_session(session_id: str):
    url = f"{settings.TYPEBOT_API_URL}/api/v1/typebots/{settings.TYPEBOT_FLOW_ID}/startChat"
    payload = {
        "isKeepSessionHistoryEnabled": True,
        "sessionId": session_id
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def send_reply(session_id: str, message: str):
    url = f"{settings.TYPEBOT_API_URL}/api/v1/sessions/{session_id}/continueChat"
    payload = {
        "message": message
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()