# AI Software Engineer – Repository Analysis Agent

An AI-powered system that analyzes a GitHub repository and allows users to ask questions about the codebase using a local Large Language Model (LLM).

This project combines **code indexing, vector embeddings, repository structure analysis, and LLM reasoning** to help developers understand unfamiliar repositories quickly.

---

# Problem Statement

Understanding a new codebase is often time-consuming. Developers need to:

* Explore multiple files
* Understand project structure
* Locate relevant functions or classes
* Read documentation (which may be incomplete)

For large repositories, this process can take **hours or even days**.

There is a need for an **intelligent system that can analyze repositories automatically and answer questions about the codebase.**

---

# Solution

This project builds an **AI-powered repository analysis agent** that:

1. Clones a GitHub repository
2. Scans and indexes source code
3. Breaks code into chunks
4. Generates vector embeddings
5. Stores them in a vector database
6. Builds a repository structure map
7. Uses a local LLM to answer questions about the repository

The result is an **AI assistant that understands the codebase and helps developers explore it faster.**

---

# System Architecture

Pipeline:

GitHub Repository
↓
Clone Repository
↓
Scan Source Files
↓
Code Chunking
↓
Embedding Generation
↓
Vector Database Storage
↓
Repository Graph Generation
↓
User Questions
↓
LLM Response using Retrieved Code Context

---

# Project Structure

```
AI-Software-Engineer
│
├── src
│   ├── analyzer
│   │   └── repo_graph.py        # Builds repository structure map
│   │
│   ├── indexer
│   │   ├── chunker.py           # Splits code into chunks
│   │   └── embedder.py          # Generates embeddings
│   │
│   ├── rag
│   │   └── retriever.py         # Retrieves relevant code chunks
│   │
│   ├── llm
│   │   └── generator.py         # LLM prompt + answer generation
│   │
│   ├── main.py                  # Repo indexing pipeline
│   └── ask_repo.py              # Ask questions about the repo
│
├── data/                        # Generated repo data (ignored in git)
├── vector_db/                   # Vector database
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Technologies Used

* Python
* Transformers
* ChromaDB
* Sentence Transformers
* PyTorch

Embeddings Model:
sentence-transformers/all-MiniLM-L6-v2

LLM:
bigcode/starcoderbase-1b
(I used this model as it is light and can run on my laptop, you can replace it with a appropriate highly trained model according to your pc/laptop/cloud specs)

---

# Installation

Clone the repository:

```
git clone https://github.com/sharduljadhavv/seb.git
cd seb
```

Create a virtual environment:

```
python -m venv venv
```

Activate it.

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# How to Run the Project

## Step 1: Index a GitHub Repository

Run:

```
python src/main.py
```

You will be prompted to enter a GitHub repository URL.

Example:

```
Paste GitHub repo URL: https://github.com/user/repository
Is this a private repo? (y/n): n
```

The system will:

* Clone the repository
* Scan the files
* Generate embeddings
* Build a repository graph
* Store data for querying

---

## Step 2: Ask Questions About the Repository

After indexing the repository, run:

```
python src/ask_repo.py
```

Example usage:

```
Ask about the repo: What does this repository do?

Ask about the repo: How does the authentication system work?

Ask about the repo: Where is the API logic implemented?
```

The AI will analyze the indexed code and return an answer.

---

# Example Use Cases

* Quickly understand unfamiliar repositories
* Explore open-source projects
* Assist developers in navigating large codebases
* Build AI developer tools

---

# Future Improvements

Possible improvements include:

* Support for multiple repositories
* Autonomous repository exploration
* File-level reasoning agents
* Web interface
* Integration with IDEs
* Better instruction-tuned LLMs
* Higher quality llms

---
