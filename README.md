# 🎥 YouTube RAG ChatBot

A production-style **Retrieval-Augmented Generation (RAG)** chatbot that answers questions about any YouTube video using its transcript.

Instead of relying only on an LLM's knowledge, the chatbot retrieves the most relevant transcript chunks using **FAISS** and supplies them as context to the LLM, resulting in more accurate and grounded answers.

---

## 🚀 Features

- 📺 Load transcripts directly from YouTube
- ✂️ Intelligent document chunking
- 🔍 Semantic search using FAISS
- 🧠 Hugging Face Embeddings
- 🤖 Qwen 2.5 Instruct LLM
- 💬 Interactive command-line chatbot
- 🏗️ Modular production-style architecture
- ⚡ Easily extensible to PDFs, websites, and documents

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| LangChain | RAG Pipeline |
| Hugging Face | LLM & Embeddings |
| FAISS | Vector Database |
| Sentence Transformers | Embedding Model |
| YouTube Transcript API | Transcript Extraction |
| dotenv | Environment Variables |

---

# Project Architecture

```
User Question
      │
      ▼
Retriever
      │
      ▼
FAISS Vector Store
      ▲
      │
Transcript Chunks
      ▲
      │
Text Splitter
      ▲
      │
YouTube Transcript
      │
      ▼
Large Language Model
      │
      ▼
Final Answer
```

---

# Project Structure

```
YouTube_RAG_ChatBot/

│
├── chunking/
│   └── chunker.py
│
├── embeddings/
│   └── embed.py
│
├── ingestion/
│   └── loader.py
│
├── llm/
│   └── model.py
│
├── prompt/
│   └── prompt_temp.py
│
├── retrieval/
│   └── retriever.py
│
├── vector_store/
│   └── faiss_store.py
│
├── tests/
│
├── .env
├── .gitignore
├── main.py
└── requirements.txt
```

---

# Pipeline

```
YouTube Video
      │
      ▼
Load Transcript
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Create FAISS Index
      │
      ▼
Retriever
      │
      ▼
Prompt Template
      │
      ▼
Qwen LLM
      │
      ▼
Answer
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/alobroke/YouTube_RAG_ChatBot.git

cd YouTube_RAG_ChatBot
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

---

# Run

```bash
python main.py
```

---

# Example

Input

```
Question:
Explain RAG
```

Output

```
RAG stands for Retrieval-Augmented Generation.

It combines retrieval systems with Large Language Models
to generate context-aware and accurate responses.
```





https://github.com/alobroke

---

## ⭐ If you found this project useful, consider giving it a star!
