from fastapi import APIRouter
from fastapi.security import HTTPBearer

router = APIRouter(prefix="/auth", tags=["Authentication"])
security = HTTPBearer()

@router.post("/login")
def login():
    return {"message": "Login successful"}