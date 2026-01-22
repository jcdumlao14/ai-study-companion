from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from app.schemas.user import User, UserCreate, TokenData

# Mock in-memory database
users_db = {}
user_id_counter = 1

SECRET_KEY = "your-secret-key"  # In production, use environment variable
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_password(plain_password, hashed_password):
    return plain_password == hashed_password

def get_password_hash(password):
    return password  # Mock: no hashing

def get_user(username: str):
    for user in users_db.values():
        if user['username'] == username:
            return user
    return None

def authenticate_user(username: str, password: str):
    user_dict = get_user(username)
    if not user_dict:
        return False
    if not verify_password(password, user_dict['password']):
        return False
    return User(**{k: v for k, v in user_dict.items() if k != 'password'})

def create_user(user: UserCreate):
    if get_user(user.username):
        return None
    global user_id_counter
    hashed_password = get_password_hash(user.password)
    user_dict = user.model_dump()
    user_dict['id'] = user_id_counter
    user_dict['password'] = hashed_password
    user_dict['score'] = 0
    db_user = User(**{k: v for k, v in user_dict.items() if k != 'password'})
    users_db[user_id_counter] = user_dict
    user_id_counter += 1
    return db_user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return None
        token_data = TokenData(username=username)
        return token_data
    except JWTError:
        return None