from services.evolution import client as evolution_client
from memory import memory_manager
from services.supabase import database as db

def handle_webhook(body: dict):
    try:
        if body.get("event") != "messages.upsert":
            return {"status": "ignored", "reason": "Evento não suportado"}

        data = body.get("data", {})
        key = data.get("key", {})
        
        if key.get("fromMe"):
            return {"status": "ignored", "reason": "Mensagem própria"}

        remote_jid = key.get("remoteJid", "")
        sender_number = remote_jid.split("@")[0] if "@" in remote_jid else remote_jid
        push_name = data.get("pushName", "Utilizador")
        
        message_obj = data.get("message", {})
        user_message = message_obj.get("conversation") or message_obj.get("extendedTextMessage", {}).get("text")

        if not user_message or not sender_number:
            return {"status": "ignored", "reason": "Mensagem vazia ou sem remetente"}

        # Registar utilizador e mensagem na base de dados
        db.get_or_create_user(sender_number, push_name)
        db.log_message(sender_number, "user", user_message)

        # Simular presença ("A escrever...")
        evolution_client.send_presence(sender_number)

        # Resposta do PETRIS
        bot_response = f"Olá, {push_name}! Sou o PETRIS. Recebi a tua mensagem: '{user_message}'"

        # Guardar na memória e na BD
        memory_manager.save_interaction(sender_number, user_message, bot_response)
        db.log_message(sender_number, "assistant", bot_response)

        # Enviar resposta via WhatsApp
        evolution_client.send_text_message(sender_number, bot_response)

        return {"status": "success"}
    except Exception as e:
        print(f"Erro no webhook do Evolution: {e}")
        raise e