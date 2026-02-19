from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI(title="Groq Chatbot API")

app.include_router(chat_router)

@app.get("/")
def health():
    return {"status": "ok"}