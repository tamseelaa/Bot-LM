# Local RAG Application with LangChain, Ollama & Chroma
## Requirements

Before starting, make sure you have:

- Python 3.10+
- Git
- Ollama
- A machine capable of running the selected Ollama models

## 1. Create the Project

Create a project folder and open it in your editor or terminal.

```shell```
mkdir project name
cd project name
## 2. Create the virtual environment
python -m venv venv
source venv/bin/activate (mac) or venv\Scripts\activate (window)
pip install langchain langchain-ollama langchain-chroma
# RAG Flow

Documents
    ↓
Embedding Model
    ↓
Vector Embeddings
    ↓
Chroma Vector Store

User Question
    ↓
Embedding Model
    ↓
Question Vector
    ↓
Similarity Search
    ↓
Relevant Documents
    ↓
Prompt + Relevant Documents + Question
    ↓
Llama 3.2
    ↓
Generated Answer
