from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    is_active: bool
    role: str

    class Config: 
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token = str
    token_type: str = "bearer"