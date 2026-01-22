from pydantic import BaseModel
from .user import User

class LeaderboardEntry(BaseModel):
    rank: int
    user: User