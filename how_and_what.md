User provides GitHub repo
        ↓
main.py
        ↓
Clone repo
        ↓
Chunk code
        ↓
Generate embeddings
        ↓
Store in vector database
        ↓
Build repo structure map
        ↓
User asks question
        ↓
ask_repo.py
        ↓
Retriever finds relevant code
        ↓
LLM generates explanation







1️⃣ main.py — Project Entry Point

File: src/main.py

Purpose: 

This is the main pipeline orchestrator that runs the entire indexing process.
It coordinates all the modules in the project.

What it does step-by-step

1) Accepts a GitHub repository URL from the user

Example input: https://github.com/sharduljadhavv/llm

2) Calls the repository cloning module

github.repo_cloner.clone_repo()

This downloads the repository locally.
Example location:

data/repos/<llm>

3) Scans the repository files

It looks for source code files like:
(*currently only python files)

.py
.js
.ts

4) Sends files to the chunking system

indexer.chunker.split_text()

Large files are split into smaller segments.

Example: create_db.py

becomes

chunk 1
chunk 2
chunk 3

But these chunks are meaningful, it makes chunks of functions, class, file name, text
This improves search quality and give meaningful context for llm to understand.

5) Sends chunks to the embedding generator

indexer.embedder.embed_text()

Each chunk is converted into a vector embedding.

Example vector: [0.12, -0.42, 0.91, ...]

These vectors represent semantic meaning of the code.

6) Stores embeddings in the vector database

Using ChromaDB

Location: vector_db/

Each stored entry contains:

{
  code_chunk,
  embedding_vector,
  metadata
}

This enables semantic search later.

7) Builds repository structure map

analyzer.repo_graph.build_repo_graph()

This analyzes the repository and extracts:

files
functions
classes

Example output: repo_map.json

Example structure:

{
 "create_db.py": {
   "functions": ["main", "generate_data_store"],
   "classes": []
 }
}

This helps the LLM understand how the repository is organized.

8) Indexing finishes

At this point the repository is fully prepared for querying.

Output message:

Repository indexed successfully!


PHASE 2 — Asking Questions

This phase runs when you execute:

python src/ask_repo.py

This is the interactive AI interface.

1) ask_repo.py — Interactive Question Interface

File: src/ask_repo.py

Purpose: Allows users to ask natural language questions about the repository.

Example questions:

What does this repo do?
How is authentication implemented?
Where is the database created?
Explain the main workflow
What happens internally

The script runs an infinite loop:

while True:

Each iteration:

1️⃣ User enters a question

Ask about the repo:

2️⃣ Question is sent to the retriever

retrieve_code(question)
3️⃣ rag/retriever.py — Semantic Code Search

File: src/rag/retriever.py

Purpose: Finds relevant code snippets related to the user's question.

Step 1 — Convert question to embedding
embed_text(question)

Example: "How is database created?"

becomes [0.13, -0.22, 0.77, ...]

Step 2 — Query vector database
collection.query()

ChromaDB searches for similar vectors.

Step 3 — Retrieve top results

Example results:

create_db.py → generate_data_store()
create_db.py → save_to_chroma()

These are returned as code chunks.

4️⃣ indexer/embedder.py — Embedding Generator

File: src/indexer/embedder.py
Purpose: Converts text/code into embeddings.

Uses model: sentence-transformers/all-MiniLM-L6-v2

What it does: text → transformer model → vector embedding

Example: "def save_to_chroma()"

becomes [0.15, -0.39, 0.28 ...]

These vectors allow semantic similarity comparison.

5️⃣ llm/generator.py — AI Answer Generator

File: src/llm/generator.py
Purpose: Uses a Large Language Model (LLM) to generate a final explanation.

Model used: bigcode/starcoderbase-1b

What it receives

User question
+
Retrieved code snippets
+
Repository structure map
Prompt construction

The system builds a prompt like: You are an AI software engineer.

Repository structure:
{repo_map}

Relevant code:
{code_chunks}

Question:
{user_question}

Explain clearly:
LLM processing

The model reads:

repo structure
+
code context
+
question

Then generates a natural language explanation.

Example output
The repository builds a RAG pipeline.

The file create_db.py creates embeddings and stores them in ChromaDB.
The rag.py file performs retrieval of relevant documents.

6️⃣ indexer/chunker.py — Code Chunking

File: src/indexer/chunker.py
Purpose: Splits large source files into smaller chunks.

Why?

LLMs and vector databases perform better with smaller context windows.

Example: 1000 line file

becomes:

chunk_1 (lines 1-200)
chunk_2 (lines 200-400)
chunk_3 (lines 400-600)

Each chunk is embedded separately.

7️⃣ analyzer/repo_graph.py — Repository Analyzer

File: src/analyzer/repo_graph.py
Purpose: Builds a structural map of the repository.

It extracts:

functions
classes
files

Example result: repo_map.json

This provides high level repository understanding to the LLM.

Final System Flow

Complete pipeline:

main.py
   │
   ├── clone repository
   │
   ├── chunk code
   │
   ├── generate embeddings
   │
   ├── store embeddings (ChromaDB)
   │
   └── build repo graph
         │
         ▼
ask_repo.py
         │
         ├── user asks question
         │
         ├── retriever finds code
         │
         ├── generator builds prompt
         │
         └── LLM generates explanation