from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.services.answer_service import AnswerService

router = APIRouter()


class ChatRequest(BaseModel):
    question: str




@router.post("/ask")
def ask_question(payload: ChatRequest):

    return AnswerService.ask(question=payload.question)