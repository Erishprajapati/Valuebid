from fastapi import FastAPI
from app.database.connection import engine,Base
from app.routers import auth, users, items, bids
app = FastAPI() #creating app to start 

Base.metadata.create_all(bind = engine)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(items.router)
app.include_router(bids.router)