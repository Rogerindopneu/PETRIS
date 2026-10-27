import os
from dotenv import load_dotenv, set_key

# Caminho para o ficheiro .env
ENV_PATH = ".env"

# Carrega as variáveis do .env se existir
load_dotenv(ENV_PATH)

def setup_gemini_api_key():
    """Verifica se a API Key do Gemini existe. Se não existir, solicita no terminal e salva no .env."""
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("\n==================================================")
        print("🤖 [CONFIGURAÇÃO INICIAL DO PETRIS]")
        print("Nenhuma API Key do Gemini foi encontrada no arquivo .env.")
        api_key = input("👉 Por favor, insira a sua API Key do Gemini: ").strip()
        
        while not api_key:
            api_key = input("❌ A chave não pode ser vazia. Insira a API Key: ").strip()
            
        # Cria o ficheiro .env se não existir
        if not os.path.exists(ENV_PATH):
            open(ENV_PATH, "w", encoding="utf-8").close()
            
        # Salva a chave no .env para as próximas execuções
        set_key(ENV_PATH, "GEMINI_API_KEY", api_key)
        os.environ["GEMINI_API_KEY"] = api_key
        print("✅ API Key do Gemini salva com sucesso no .env!")
        print("==================================================\n")
        
    return api_key

class Settings:
    PORT: int = int(os.getenv("PORT", 3000))
    ENV: str = os.getenv("NODE_ENV", "development")
    
    # Evolution API
    EVOLUTION_API_URL: str = os.getenv("EVOLUTION_API_URL", "")
    EVOLUTION_API_KEY: str = os.getenv("EVOLUTION_API_KEY", "")
    EVOLUTION_INSTANCE_NAME: str = os.getenv("EVOLUTION_INSTANCE_NAME", "petris")
    
    # Typebot
    TYPEBOT_API_URL: str = os.getenv("TYPEBOT_API_URL", "")
    TYPEBOT_FLOW_ID: str = os.getenv("TYPEBOT_FLOW_ID", "")
    
    # Supabase
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_SERVICE_ROLE_KEY: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")
    
    # Gemini AI
    GEMINI_API_KEY: str = ""

settings = Settings()