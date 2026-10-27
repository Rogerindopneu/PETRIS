import os
import subprocess
import sys

def main():
    print(" [CONFIGURAÇÃO E INSTALAÇÃO DO PETRIS]")

    # 1. Instalar dependências do requirements.txt
    print("\n Instalando dependências...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

    # 2. Configurar o arquivo .env
    env_path = ".env"
    if not os.path.exists(env_path):
        print("\n Configurando variáveis de ambiente...")
        api_key = input(" Insira a sua API Key do Gemini: ").strip()
        
        with open(env_path, "w", encoding="utf-8") as f:
            f.write(f"GEMINI_API_KEY={api_key}\n")
            f.write("PORT=3000\n")
        print(" Ficheiro .env criado com sucesso!")
    else:
        print("\n Ficheiro .env já existente.")

    print("\n Configuração concluída! Para iniciar o assistente, execute:")
    print(" py main.py\n")

if __name__ == "__main__":
    main()