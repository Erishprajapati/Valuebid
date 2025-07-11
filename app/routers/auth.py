from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut, UserLogin, Token
from app.models.user import User
from app.services.auth import hash_password, verify_password, create_access_token
from app.database.connection import get_db

router = APIRouter(prefix='/auth', tags = ["Auth"])
@router.post('/register', response_model = UserOut)
def register(user_create: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_create.username).first()
    if user:
        raise HTTPException(status_code=400, detail = "Username already exists")
    hashed_pwd = hash_password(user_create.password)
    new_user = User(
        username = user_create.username,
        email = user_create.email,
        hashed_password = hashed_pwd,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post('/login', response_model=Token)
def login(user_login: UserLogin, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_login.username).first()
    if not user or not verify_password(user_login.password, user.hashed_password):
        raise HTTPException(status_code=401, detail = "Invalid credentials")
    access_token = create_access_token(data = {"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
