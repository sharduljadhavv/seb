import chromadb

client = chromadb.Client()

collection = client.get_or_create_collection(name="repo_index")


def store_embeddings(chunks, embeddings):

    documents = []
    metadatas = []
    ids = []

    for i, chunk in enumerate(chunks):

        documents.append(chunk["text"])
        metadatas.append({"file": chunk["file"]})
        ids.append(str(i))

    collection.add(
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings,
        ids=ids
    )