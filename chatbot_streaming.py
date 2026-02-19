import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

# System prompt (AI personality)
system_prompt = """
You are a senior backend and ML engineer mentor.
Explain concepts clearly with examples and best practices.
"""

messages = [
    {"role": "system", "content": system_prompt}
]

print("Groq AI Backend Mentor (type 'exit' to quit)")

while True:
    user = input("\nYou: ")
    
    # Exit Command
    if user.lower() =="exit":
        break
    
    # Clear Memory Command
    if user == "/clear":
        messages = [{"role": "system", "content": system_prompt}]
        print("Memory cleared.")
        continue    
    
    messages.append({"role": "user", "content": user})
    
    # Streaming response
    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        stream=True,
    )
    
    print("AI: ", end="", flush=True)
    ai_response = ""
    
    for chunk in stream:
        if chunk.choices[0].delta.content:
            token = chunk.choices[0].delta.content
            print(token, end="", flush=True)
            ai_response += token
    
    messages.append({"role": "assistant", "content": ai_response})