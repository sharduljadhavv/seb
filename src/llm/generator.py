from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import json
import os

MODEL_NAME = "bigcode/starcoderbase-1b"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print("Loading LLM:", MODEL_NAME)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32
)


def load_repo_map():

    graph_file = os.path.join(
        BASE_DIR,
        "data",
        "repos",
        "llm",
        "repo_map.json"
    )

    try:
        with open(graph_file, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception as e:
        print("Repo graph load failed:", e)
        return {}


def generate_answer(question, retrieved_chunks):

    repo_map = load_repo_map()
    
    context = "\n\n".join(retrieved_chunks)
    
    if context.strip() == "":
        context = "No relevant code snippets were retrieved."
    

    prompt = f"""
You are a senior software engineer.

Use the repository structure and code snippets to answer the question.

Repository structure:
{repo_map}

Code snippets:
{context}

User question:
{question}

Answer:
"""

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        temperature=0.2,
        repetition_penalty=1.2,
        do_sample=True
    )

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    result = result[len(prompt):]

    return result