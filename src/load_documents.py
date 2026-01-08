import os
from langchain_community.document_loaders import TextLoader, PyPDFLoader

def load_documents(docs_path):
    documents = []

    for file in os.listdir(docs_path):
        file_path = os.path.join(docs_path, file)

        if file.endswith(".txt"):
            loader = TextLoader(file_path, encoding="utf-8")
            documents.extend(loader.load())

        elif file.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())

    return documents
