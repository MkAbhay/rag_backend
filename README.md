# RAG Backend

A Retrieval-Augmented Generation (RAG) backend built with Python, FastAPI, and LangChain. This service ingests PDF and DOCX documents, builds semantic embeddings in ChromaDB, and answers user questions using OpenAI with context retrieved from the uploaded documents.

## Features

- Document ingestion for `.pdf` and `.docx` files
- Automatic document parsing and chunking with LangChain loaders
- Semantic embedding using OpenAI embeddings (`text-embedding-3-small`)
- Persistent vector store via ChromaDB
- Question-answering with retrieval from document chunks
- Answers include source metadata and token usage
- FastAPI auto-generated API docs at `/docs` and `/redoc`
- Health check endpoint at `/`

## Tech Stack

- Python
- FastAPI
- Uvicorn
- LangChain
- OpenAI embeddings and ChatOpenAI
- ChromaDB (via `langchain_chroma`)
- `tiktoken` for token counting
- `python-dotenv` for environment configuration
- `langchain-community` loaders for PDF and DOCX support

## Directory Structure

- `app/main.py` — FastAPI app entrypoint
- `app/api/routes/chat.py` — chat/question-answer API
- `app/api/routes/documents.py` — document upload API
- `app/rag/services/answer_service.py` — query/retrieval and answer composition
- `app/rag/services/ingestion_service.py` — document ingestion and vector insertion
- `app/rag/vectorstore/chroma_client.py` — Chroma persistent store configuration
- `app/rag/retrievers/vector_retriever.py` — retrieval pipeline
- `app/rag/prompt/ask.py` — prompt template for the LLM
- `app/rag/llm/openai.py` — OpenAI chat model configuration
- `app/rag/loaders` — document loaders for PDF and DOCX
- `app/rag/chucking/chunk_service.py` — document chunking logic

## Setup

1. Create a Python virtual environment from the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and set:

```dotenv
OPENAI_API_KEY=your_openai_api_key
CHROMA_COLLECTION=your_collection_name
CHROMA_DB_PATH=./chroma_db
```

4. Start the server:

```powershell
uvicorn app.main:app --reload
```

## API Reference

### Health check

- `GET /`
- Returns service status.

Example:

```json
{
  "status": "running"
}
```

### Upload Document

- `POST /documents/upload`
- Uploads a `.pdf` or `.docx` file, parses it, chunks it, and stores embeddings in Chroma.
- The endpoint stores uploads in `uploads/` and returns the document ID and chunk count.

Request example using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/documents/upload" \
  -F "file=@path/to/document.pdf"
```

Response example:

```json
{
  "document_id": "<uuid>",
  "chunks": 12
}
```

### Ask Question

- `POST /chat/ask`
- Sends a user question to the retrieval pipeline.
- The system fetches the top matching chunks from Chroma, formats the prompt, and queries OpenAI.
- Returns the answer text, prompt contents, token count, and source metadata.

Request example:

```bash
curl -X POST "http://127.0.0.1:8000/chat/ask" \
  -H "Content-Type: application/json" \
  -d '{"question": "What does the document say about X?"}'
```

Response example:

```json
{
  "answer": "...",
  "prompt": "...",
  "tokens": 123,
  "sources": [
    {
      "document_id": "...",
      "chunk_id": "..."
    }
  ]
}
```

## FastAPI Documentation

Once the server is running, view interactive API docs at:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

## Usage Notes

- Only `.pdf` and `.docx` uploads are supported.
- Uploaded files are saved under the `uploads/` directory.
- Document chunks are stored in ChromaDB for retrieval.
- `CHROMA_DB_PATH` should point to a writable folder for persistent storage.
- The app uses `gpt-4.1-mini` with `temperature=0` for deterministic answers.

## Troubleshooting

- If `uvicorn` reports module import errors, confirm the command uses the dotted module path:

```powershell
uvicorn app.main:app --reload
```

- If environment variables are missing, validate `.env` and restart the app.
- If documents fail to upload, verify the file extension is `.pdf` or `.docx`.

## License

This project does not include a license file by default. Add one if you want to share or publish the code.
