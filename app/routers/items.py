from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
def get_users():
    return {"message": "Items route working"}
