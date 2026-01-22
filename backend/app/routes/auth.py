from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.schemas.user import UserCreate, Token, LoginRequest, User
from app.services.auth_service import authenticate_user, create_user, create_access_token, verify_token
from datetime import timedelta

router = APIRouter()
security = HTTPBearer()

@router.post("/login", response_model=Token)
def login(user_credentials: LoginRequest):
    user = authenticate_user(user_credentials.username, user_credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/signup", response_model=Token)
def signup(user: UserCreate):
    db_user = create_user(user)
    if not db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": db_user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token_data = verify_token(credentials.credentials)
    if token_data is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    from app.services.auth_service import get_user
    user_dict = get_user(token_data.username)
    if not user_dict:
        raise HTTPException(status_code=401, detail="User not found")
    return User(**{k: v for k, v in user_dict.items() if k != 'password'})