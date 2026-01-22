from app.schemas.leaderboard import LeaderboardEntry
from app.schemas.user import User
from .auth_service import users_db

def get_leaderboard():
    users = [User(**{k: v for k, v in user.items() if k != 'password'}) for user in users_db.values()]
    sorted_users = sorted(users, key=lambda u: u.score, reverse=True)
    leaderboard = []
    for rank, user in enumerate(sorted_users, start=1):
        leaderboard.append(LeaderboardEntry(rank=rank, user=user))
    return leaderboard