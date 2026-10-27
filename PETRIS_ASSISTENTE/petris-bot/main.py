from fastapi import FastAPI, Request
from config.settings import settings, setup_gemini_api_key
from services.evolution.webhook import handle_webhook

app = FastAPI(title="PETRIS Bot")

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "PETRIS Bot Python"}

@app.post("/webhook/evolution")
async def evolution_webhook(request: Request):
    body = await request.json()
    result = handle_webhook(body)
    return {"success": True, "result": result}

if __name__ == "__main__":
    # Executa a verificação/solicitação da chave do Gemini na primeira execução
    settings.GEMINI_API_KEY = setup_gemini_api_key()
    
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=True)