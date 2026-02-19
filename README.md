# LLM Backend Platform

A production-style backend platform for Large Language Model (LLM) applications built using **Groq, FastAPI, and Python**.  
This project demonstrates **LLM system design, scalable backend architecture, and AI service engineering**.

---

## 🚀 Key Features

### CLI Chatbots

- Basic conversational chatbot using Groq Llama 3
- Streaming chatbot with real-time token streaming
- Conversation memory handling
- Secure environment-based configuration

### API Backend (In Progress)

- FastAPI-based AI service layer
- REST endpoints for LLM inference
- Modular service architecture (config, routes, services, models)

### Planned Advanced Features

- RAG (Retrieval-Augmented Generation) with vector database
- Agentic AI workflows
- Conversation memory with Redis
- Docker & Cloud deployment
- Rate limiting & authentication

---

## 🏗️ Architecture Overview

```text
Client (CLI / UI / Postman)
|
v
FastAPI Gateway
|
v
LLM Service Layer (Groq)
|
v
Memory Store / Vector DB (Planned)
```

---

## 📂 Project Structure

```text
llm-backend-platform/
│
├── chatbot_basic/ # Basic CLI chatbot
├── chatbot_streaming/ # Streaming chatbot
├── app/ # FastAPI backend
│ ├── main.py
│ ├── routes/
│ ├── services/
│ ├── models/
│ └── core/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧠 Versions

| File                   | Description                          |
| ---------------------- | ------------------------------------ |
| `chatbot_basic.py`     | Simple Groq chatbot with memory      |
| `chatbot_streaming.py` | Streaming chatbot with system prompt |

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

# Activation (Windows)

```bash
.\venv\Scripts\activate
```

```bash
pip install -r requirements.txt

```

---

### 2️⃣ Add Groq API Key

- Create a .env file:
  GROQ_API_KEY=your_api_key_here

Or rename: .env.example .env

---

▶️ Run the Chatbot

```bash
python chatbot_basic/chatbot_basic.py

```

Or streaming version:

```bash
python chatbot_streaming/chatbot_streaming.py

```

---

### Running the FastAPI Backend

```bash
uvicorn app.main:app --reload

```

## Open Swagger UI:

```bash
http://127.0.0.1:8000/docs

```

---

### 📌 Why This Project

This project demonstrates:

- Integration of LLM APIs in backend systems
- Modular Python architecture for AI services
- Real-time AI streaming responses
- Secure configuration management using environment variables
- This repository will later be extended with FastAPI APIs, RAG pipelines, and agentic AI workflows to showcase \* \* ML system engineering skills.

---

### 📈 Roadmap

- [&check;] CLI chatbot (basic)
- [&check;] Streaming chatbot (streaming)
- [ ] FastAPI inference API
- [ ] Redis-based conversation memory
- [ ] RAG with vector embeddings
- [ ] Agentic AI workflows
- [ ] Docker containerization
- [ ] Cloud deployment (AWS/GCP)

---

### 🧑‍💻 Author

- Vishal Sinha
- Backend Engineer transitioning into ML & GenAI Engineering
