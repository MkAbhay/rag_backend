import os
import uuid

from fastapi import APIRouter, UploadFile

from app.rag.services.ingestion_service import IngestionService

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile):

    document_id = str(uuid.uuid4())

    extension=os.path.splitext(file.filename)[1].lower()
    print(f"Received file: {file.filename} with extension: {extension}")

    file_path = f"{UPLOAD_DIR}/{file.filename}"
    print(f"Saving uploaded file to: {file_path}")

    with open(file_path, "wb") as f:
        f.write(await file.read())

    result = IngestionService.ingest_document(
        path=file_path,
        document_id=document_id,
        extension=extension
    )

    return result