from rag.retriever import retrieve_code
from llm.generator import generate_answer


while True:

    question = input("\nAsk about the repo: ")

    if question.lower() == "exit":
        break

    retrieved = retrieve_code(question)

    chunks = retrieved["documents"][0]

    answer = generate_answer(question, chunks)

    print("\nAI Answer:\n")
    print(answer)