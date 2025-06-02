from fastapi import FastAPI
from pydantic import BaseModel
from backend.rag import query_rag

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/chat")
def chat(query: Query):
    answer = query_rag(query.question)
    return {"answer": answer.strip()}
