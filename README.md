# 📄 RAG Chatbot with CodeLlama GGUF

This project is a Retrieval-Augmented Generation (RAG) chatbot that can read documents and answer questions using the CodeLlama-7b model in GGUF format. It integrates `llama.cpp`, `LangChain`, `FAISS`, and `FastAPI`, with an optional Streamlit interface for local interaction.

---

## 🔧 Features

- 🧠 Local LLM Inference using `llama.cpp`
- 📚 Multi-format document ingestion (PDF, DOCX)
- 🔍 Semantic document search using FAISS
- 💬 Natural question-answering from documents
- ⚡ FastAPI backend for API access
- 🎨 Streamlit frontend for UI chatbot (optional)

---

## 📁 Project Structure

```
rag-chatbot-codellama/
├── models/                     # Place your .gguf LLM model here
├── docs/                       # Add your PDF/DOCX documents here
├── vectorstore/faiss_index/   # FAISS index created from documents
├── backend/
│   ├── llm_loader.py          # Load CodeLlama GGUF with llama.cpp
│   └── rag.py                 # RAG logic: load documents, embed, search, ask
├── app/
│   └── api.py                 # FastAPI endpoint
├── streamlit_app.py           # Optional Streamlit frontend
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Install Requirements

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### 2. Add Model & Documents

- Place your CodeLlama GGUF model here:
  ```
  models/CodeLlama-7b-hf_Q4_K_M.gguf
  ```

- Add your documents to the `docs/` folder.

### 3. Build Vector Store

```bash
python backend/rag.py --build
```

This loads documents, splits them, embeds them, and saves the FAISS index.

### 4. Run the FastAPI Backend

```bash
uvicorn app.api:app --reload
```

API Example:

```bash
curl -X POST http://127.0.0.1:8000/chat \
    -H "Content-Type: application/json" \
    -d '{"question": "What is the purpose of this document?"}'
```

### 5. (Optional) Run Streamlit UI

```bash
streamlit run streamlit_app.py
```

---

## 🧠 How It Works

1. **Document Loading**: Loads PDF/DOCX files from `docs/`
2. **Text Splitting**: Breaks documents into smaller chunks
3. **Embedding**: Uses `sentence-transformers` to convert text into vectors
4. **Vector Store**: Stores chunks in FAISS for semantic search
5. **Question Answering**:
   - Finds relevant chunks for the question
   - Combines chunks with question as prompt
   - Sends prompt to `llama.cpp`-based CodeLlama
   - Returns answer

---

## 🛠 Tech Stack

- [llama.cpp](https://github.com/ggerganov/llama.cpp)
- [LangChain](https://python.langchain.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [sentence-transformers](https://www.sbert.net/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)

---

## 📦 Deployment Options

| Option       | Description                                 |
|--------------|---------------------------------------------|
| Localhost    | Run on CPU or GPU locally                   |
| Docker       | Containerize with FastAPI + Streamlit       |
| RunPod       | GPU-based inference online                  |
| GCP/AWS VM   | Production LLM API or web app               |

---

## 📬 Contact

Built with ❤️ by Budi Setiawan  
For custom deployments, enhancements, or integrations — reach out!

---

