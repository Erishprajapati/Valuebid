from fastapi import APIRouter

router = APIRouter()

@router.get("/bids")
def get_users():
    return {"message": "Bids route working"}
