from fastapi import APIRouter, Depends
from typing import List
from app.schemas.leaderboard import LeaderboardEntry
from app.services.leaderboard_service import get_leaderboard
from .auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[LeaderboardEntry])
def get_leaderboard_route(current_user=Depends(get_current_user)):
    return get_leaderboard()