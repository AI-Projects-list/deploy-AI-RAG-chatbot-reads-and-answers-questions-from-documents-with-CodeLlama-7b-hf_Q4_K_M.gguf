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

## 📈 Evaluation Methods for the Chatbot

To ensure that the chatbot built using CodeLlama and RAG performs accurately and efficiently, evaluation is divided into four major parts:

---

### 🧪 1. Functional Evaluation (Manual QA Testing)

**Goal:** Check if the chatbot gives correct and coherent answers.

**Steps:**
- Prepare 10–20 questions based on your documents.
- Ask those questions via API or Streamlit.
- Manually verify if the answers are:
  - Relevant
  - Factual
  - Complete

```python
questions = [
    "What is the warranty period?",
    "What safety measures are mentioned?"
]

for q in questions:
    answer = query_rag(q)
    print(f"Q: {q}\nA: {answer}\n{'-'*40}")
```

---

### 🔍 2. Retrieval Evaluation (Search Accuracy)

**Goal:** Ensure that the correct document chunks are retrieved for each query.

**Metrics:**
- **Top-k accuracy:** Does the correct chunk appear in the top-k?
- **Recall@k:** Ratio of relevant retrieved chunks.
- **Precision@k:** Ratio of retrieved chunks that are relevant.

**Implementation Example:**

```python
db = load_vectorstore()
query = "What is the warranty period?"
results = db.similarity_search(query, k=3)

for i, doc in enumerate(results):
    print(f"Rank {i+1}: {doc.page_content[:150]}...")
```

Manually verify that at least one chunk is relevant to the query.

---

### 🧠 3. Generation Evaluation (Answer Quality)

**Goal:** Evaluate how well the model answers based on retrieved content.

**Metrics:**
- **BLEU/ROUGE scores:** Compare LLM output to a reference answer.
- **LLM-assisted review:** Use GPT-4 to review answers and score them.

**Manual Scoring Rubric (1-5 scale):**
| Criterion   | 1 = Poor | 5 = Excellent |
|-------------|----------|---------------|
| Relevance   | ❌        | ✅             |
| Clarity     | ❌        | ✅             |
| Factualness | ❌        | ✅             |
| Helpfulness | ❌        | ✅             |

```python
# Example human eval structure
qa_pairs = [
    {"question": "What is the warranty?", "expected": "1-year warranty", "answer": "The product has a 1-year warranty."},
]

for qa in qa_pairs:
    print("Q:", qa["question"])
    print("Expected:", qa["expected"])
    print("LLM Answer:", qa["answer"])
    print("Score yourself from 1–5")
```

---

### ⏱️ 4. Latency and Performance

**Goal:** Measure system responsiveness.

**Metric:** Time taken from question to full answer (end-to-end latency).

```python
import time

query = "Explain the product safety measures."
start = time.time()
response = query_rag(query)
end = time.time()

print("Answer:", response)
print("Latency:", round(end - start, 2), "seconds")
```

Track average latency across multiple runs.

---

## 🧰 Tools to Automate Evaluation

| Tool          | Use                                |
|---------------|-------------------------------------|
| LangChain Eval| Evaluate answers and retrieval     |
| Ragas         | End-to-end RAG pipeline evaluation |
| TruLens       | LLM quality, hallucination tracking |
| BLEU/ROUGE    | Similarity between output/reference |
| GPT-4 as Judge| Self-assessing correctness          |

---

## ✅ Evaluation Summary Table

| Evaluation Type  | Method         | Metric            | Implementation          |
|------------------|----------------|-------------------|--------------------------|
| Functional       | Manual QA      | Pass/Fail         | `query_rag()` + compare |
| Retrieval        | Top-k search   | Recall@k, P@k     | FAISS `similarity_search` |
| Generation       | GPT or human   | 1–5 scale or BLEU | Manual or automated     |
| Latency          | Time tracking  | Seconds           | `time.time()`           |

---
