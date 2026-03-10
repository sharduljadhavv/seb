import os


def load_repo_files(repo_path):

    code_files = []

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if file.endswith((".py", ".js", ".ts", ".java", ".go", ".rs", ".cpp")):

                path = os.path.join(root, file)

                try:
                    with open(path, "r", encoding="utf-8") as f:

                        code_files.append((path, f.read()))

                except:
                    pass

    return code_files