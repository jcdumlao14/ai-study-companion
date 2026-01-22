from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class LoginRequest(BaseModel):
    username: str
    password: str

class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr

class User(UserBase):
    id: int
    score: int = 0

class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    score: int | None = None

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    username: str | None = None