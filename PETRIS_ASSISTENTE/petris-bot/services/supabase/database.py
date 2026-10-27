from datetime import datetime
from supabase import create_client, Client
from config.settings import settings

# Inicializa como None por padrão
supabase: Client = None

# Cria a conexão apenas se as credenciais do Supabase estiverem preenchidas
if settings.SUPABASE_URL and settings.SUPABASE_SERVICE_ROLE_KEY:
    try:
        supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_SERVICE_ROLE_KEY)
    except Exception as e:
        print(f"⚠️ Aviso: Não foi possível conectar ao Supabase: {e}")

def get_or_create_user(phone: str, name: str = "Desconhecido"):
    if not supabase:
        return None
    try:
        response = supabase.table("users").select("*").eq("phone_number", phone).execute()
        if response.data:
            return response.data[0]
        
        new_user = supabase.table("users").insert({"phone_number": phone, "name": name}).execute()
        return new_user.data[0] if new_user.data else None
    except Exception as e:
        print(f"Erro em get_or_create_user: {e}")
        return None

def log_message(phone: str, sender_type: str, content: str):
    if not supabase:
        return None
    try:
        data = {
            "phone_number": phone,
            "sender_type": sender_type,
            "content": content,
            "created_at": datetime.utcnow().isoformat()
        }
        return supabase.table("messages").insert(data).execute()
    except Exception as e:
        print(f"Erro em log_message: {e}")
        return None