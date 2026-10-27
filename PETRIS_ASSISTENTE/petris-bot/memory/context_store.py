from typing import Dict, List
from datetime import datetime

# Armazenamento em memória RAM para contextos ativos
active_contexts: Dict[str, List[dict]] = {}

def get_context(user_id: str) -> List[dict]:
    if user_id not in active_contexts:
        active_contexts[user_id] = []
    return active_contexts[user_id]

def add_message(user_id: str, message: dict) -> None:
    context = get_context(user_id)
    message_data = message.copy()
    message_data["timestamp"] = datetime.utcnow().isoformat()
    context.append(message_data)
    active_contexts[user_id] = context

def clear_context(user_id: str) -> None:
    if user_id in active_contexts:
        del active_contexts[user_id]