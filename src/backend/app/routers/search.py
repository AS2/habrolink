from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
async def auth_login():
    return
