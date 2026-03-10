from github.repo_cloner import clone_repo

from indexer.repo_loader import load_repo_files
from indexer.chunker import chunk_code
from indexer.embedder import embed_text
from indexer.vector_store import store_embeddings

from analyzer.repo_graph import build_repo_graph


def run_pipeline():

    repo_url = input("Paste GitHub repo URL: ")

    is_private = input("Is this a private repo? (y/n): ")

    token = None

    if is_private.lower() == "y":
        token = input("Enter GitHub Personal Access Token: ")

    graph_path = clone_repo(repo_url, token)

    files = load_repo_files(graph_path)

    print("FILES FOUND:", len(files))

    chunks = chunk_code(files)

    embeddings = embed_text(chunks)

    store_embeddings(chunks, embeddings)

    build_repo_graph(graph_path)

    print("\nRepository indexed successfully!")


if __name__ == "__main__":
    run_pipeline()