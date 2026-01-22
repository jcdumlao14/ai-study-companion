from app.schemas.user import User, UserUpdate
from .auth_service import users_db

def get_user_by_username(username: str):
    for user in users_db.values():
        if user['username'] == username:
            return User(**{k: v for k, v in user.items() if k != 'password'})
    return None

def update_user(username: str, user_update: UserUpdate):
    for uid, user in users_db.items():
        if user['username'] == username:
            update_data = user_update.model_dump(exclude_unset=True)
            user.update(update_data)
            return User(**{k: v for k, v in user.items() if k != 'password'})
    return None