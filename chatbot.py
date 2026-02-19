import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

messages = []

print("Groq AI Chatbot (type 'exit' to quit)")

while True:
    user = input("You: ")
    if user.lower() =="exit":
        break
    
    messages.append({"role": "user", "content": user})
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
    )
    
    ai_msg = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ai_msg})
    
    print("AI:", ai_msg)