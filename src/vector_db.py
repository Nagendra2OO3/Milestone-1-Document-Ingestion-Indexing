import os
from langchain_community.vectorstores import Chroma
from load_documents import load_documents
from text_splitter import split_documents
from embeddings import get_embedding_model

def create_vector_db(docs_path, db_path):
    documents = load_documents(docs_path)
    print(f"Documents loaded: {len(documents)}")

    chunks = split_documents(documents)
    print(f"Chunks created: {len(chunks)}")

    embeddings = get_embedding_model()

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=db_path
    )

    print("✅ Vector DB created successfully")
