from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def create_embeddings(chunks):
    texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(texts)
    return embeddings


def embed_text(texts):
    embeddings = model.encode(texts)
    return embeddings