import streamlit as st
from backend.rag import query_rag

st.title("📄 Document Chatbot (CodeLlama)")

question = st.text_input("Ask your question:")
if st.button("Ask") and question:
    st.write("Thinking...")
    answer = query_rag(question)
    st.success(answer)
