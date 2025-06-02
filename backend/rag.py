from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import os

def build_vectorstore():
    loader = PyPDFLoader("docs/sample.pdf")
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)
    embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(split_docs, embedder)
    db.save_local("vectorstore/faiss_index")

def load_vectorstore():
    embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local("vectorstore/faiss_index", embedder)

def query_rag(question):
    from backend.llm_loader import get_llama_response
    db = load_vectorstore()
    docs = db.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in docs])
    prompt = f"""You are an assistant. Answer based on context.

Context:
{context}

Q: {question}
A:"""
    return get_llama_response(prompt)
