import os

from app.rag.loaders.pdf_loader import load_pdf
from app.rag.loaders.docx_loader import load_docx
from app.rag.chucking.chunk_service import chunk_documents
from app.rag.vectorstore.chroma_client import vector_store


class IngestionService:

    @staticmethod
    def ingest_document(path: str, document_id: str, extension: str = None):

        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")
        
        match extension:
            case ".docx":
                print(f"Loading DOCX document: {path}")
                documents = load_docx(path)
            case ".pdf":
                print(f"Loading PDF document: {path}")
                documents = load_pdf(path)
            case _:
                raise ValueError(f"Unsupported file type: {extension}")

        chunks = chunk_documents(documents)

        for index, chunk in enumerate(chunks):
            chunk.metadata["document_id"] = document_id
            chunk.metadata["chunk_id"] = f"{document_id}_{index}"
            chunk.metadata["source"] = path
            chunk.metadata["source_type"] = extension
            chunk.metadata["chunk_index"] = index

        vector_store.add_documents(chunks)

        return {
            "document_id": document_id,
            "chunks": len(chunks)
        }