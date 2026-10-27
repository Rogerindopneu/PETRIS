from typing import List, Optional
from memory.context_store import get_context, add_message, clear_context

MAX_MEMORY_LIMIT = 10

def get_recent_history(user_id: str) -> List[dict]:
    full_context = get_context(user_id)
    if len(full_context) > MAX_MEMORY_LIMIT:
        return full_context[-MAX_MEMORY_LIMIT:]
    return full_context

def save_interaction(user_id: str, user_message: Optional[str], bot_response: Optional[str]) -> None:
    if user_message:
        add_message(user_id, {"role": "user", "content": user_message})
    if bot_response:
        add_message(user_id, {"role": "assistant", "content": bot_response})

def reset_memory(user_id: str) -> None:
    clear_context(user_id)