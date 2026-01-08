import os
from vector_db import create_vector_db

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    DOCS_PATH = os.path.join(BASE_DIR, "data", "documents")
    DB_PATH = os.path.join(BASE_DIR, "db")

    create_vector_db(DOCS_PATH, DB_PATH)
    