from groq import Groq
from app.core.config import settings
from app.core.logger import logger

client = Groq(api_key=settings.GROQ_API_KEY)

def chat_completion(prompt: str):
    logger.info(f"LLM request: {prompt}")
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content