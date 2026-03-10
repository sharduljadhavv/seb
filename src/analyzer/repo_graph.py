import os
import json
import ast

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

graph_path = os.path.join(BASE_DIR, "data", "repo_map.json")


def analyze_file(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
    except:
        return None

    functions = []
    classes = []

    for line in code.split("\n"):

        line = line.strip()

        if line.startswith("def "):
            functions.append(line.split("(")[0].replace("def ", ""))

        if line.startswith("class "):
            classes.append(line.split("(")[0].replace("class ", ""))

        if "function " in line:
            name = line.split("function ")[1].split("(")[0]
            functions.append(name)

    return {
        "file": file_path,
        "functions": functions,
        "classes": classes
    }


def build_repo_graph(repo_path):

    repo_map = {}

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if file.endswith((".py", ".js", ".ts", ".tsx")):

                full_path = os.path.join(root, file)

                result = analyze_file(full_path)

                if result:
                    repo_map[full_path] = {
                        "functions": result["functions"],
                        "classes": result["classes"]
                    }

    graph_path = os.path.join(repo_path, "repo_map.json")

    with open(graph_path, "w", encoding="utf-8") as f:
        json.dump(repo_map, f, indent=2)

    print("Repo graph created with", len(repo_map), "files")
    print("Saved at:", graph_path)

    repo_map = {}

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if file.endswith(".py"):

                full_path = os.path.join(root, file)

                result = analyze_file(full_path)

                if result:
                    repo_map[full_path] = {
                        "functions": result["functions"],
                        "classes": result["classes"]
                    }

    with open(graph_path, "w", encoding="utf-8") as f:
        json.dump(repo_map, f, indent=2)

    print("Repo graph created with", len(repo_map), "files")