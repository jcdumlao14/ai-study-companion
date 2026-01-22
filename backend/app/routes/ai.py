from fastapi import APIRouter, Depends
from app.schemas.ai import AskRequest, AskResponse
from app.services.ai_service import ask_ai
from .auth import get_current_user

router = APIRouter()

@router.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest, current_user=Depends(get_current_user)):
    response = ask_ai(request.question)
    return AskResponse(response=response)