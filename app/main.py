from fastapi import FastAPI
from app.database.connection import Base, engine, SessionLocal

app = FastAPI()

#declaring the root of the system where user lands
@app.get("/")
def read_root():
    return {"Message": "Welcome to system"}

Base.metadata.create_all(bind = engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/create_user', tags=["user"])
def register_user(request:schemas.User, db:Session = Depends(get_db))
    