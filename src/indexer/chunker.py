import ast
import os

def chunk_code(files, chunk_size=500):

    chunks = []

    for file_path, content in files:

        lines = content.split("\n")

        for i in range(0, len(lines), chunk_size):

            chunk_text = "\n".join(lines[i:i+chunk_size])

            chunks.append({
                "text": chunk_text,
                "file": file_path
            })

    print("TOTAL CHUNKS:", len(chunks))

    return chunks





def chunk_by_lines(code: str, filename: str, max_chars: int):

    blocks = code.split("\n\n")

    chunks = []
    current = ""

    for block in blocks:

        if len(current) + len(block) > max_chars and current:

            header = f"# File: {filename}"

            chunks.append(
                {
                    "text": header + "\n\n" + current.strip(),
                    "file": filename,
                    "class": None,
                    "function": None,
                }
            )

            current = block

        else:
            current += "\n\n" + block

    if current:
        header = f"# File: {filename}"

        chunks.append(
            {
                "text": header + "\n\n" + current.strip(),
                "file": filename,
                "class": None,
                "function": None,
            }
        )

    return chunks