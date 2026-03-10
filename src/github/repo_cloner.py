import os
from git import Repo


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

BASE_REPO_PATH = os.path.join(BASE_DIR, "data", "repos")

def clone_repo(repo_url, token=None):

    if not os.path.exists(BASE_REPO_PATH):
        os.makedirs(BASE_REPO_PATH)

    repo_name = repo_url.split("/")[-1].replace(".git", "")
    repo_path = os.path.join(BASE_REPO_PATH, repo_name)

    if os.path.exists(repo_path):
        print("Repo already exists locally:", repo_path)
        return repo_path

    if token:
        repo_url = repo_url.replace(
            "https://",
            f"https://{token}@"
        )

    print("Cloning repository...")

    Repo.clone_from(repo_url, repo_path)

    print("Repo cloned to:", repo_path)

    return repo_path