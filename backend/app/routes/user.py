from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import User, UserUpdate
from app.services.user_service import get_user_by_username, update_user
from .auth import get_current_user

router = APIRouter()

@router.get("/profile", response_model=User)
def get_profile(current_user=Depends(get_current_user)):
    return current_user

@router.put("/profile", response_model=User)
def update_profile(user_update: UserUpdate, current_user=Depends(get_current_user)):
    updated_user = update_user(current_user.username, user_update)
    if not updated_user:
        raise HTTPException(status_code=400, detail="Update failed")
    return updated_user