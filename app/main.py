from fastapi import FastAPI

from app.api.routes.chat import router as chat_router
from app.api.routes.documents import router as documents_router

app = FastAPI()

app.include_router(chat_router, prefix="/chat")
app.include_router(documents_router, prefix="/documents")


@app.get("/")
def health_check():
    return {
        "status": "running"
    }