import chromadb
import os
from indexer.embedder import embed_text

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

VECTOR_DB_PATH = os.path.join(BASE_DIR, "vector_db")


client = chromadb.PersistentClient(
    path= VECTOR_DB_PATH
)

collection = client.get_or_create_collection(
    name="repo_embeddings"
)


def retrieve_code(question, top_k=3):

    query_embedding = embed_text([question])[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results