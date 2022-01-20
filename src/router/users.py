from fastapi import APIRouter, Body, Depends
from pydantic import BaseModel

from src.core.auth.bearer import JWTBearer
from src.services.auth import UserSchema, sign_jwt, UserLoginSchema, check_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


class User(BaseModel):
    username: str
    password: str


@router.post("/signup")
async def create_user(user: UserSchema = Body(...)):
    # db work
    return sign_jwt(user.email)


@router.post("/login")
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return sign_jwt(user.email)
    return {
        "error": "Wrong login details!"
    }


@router.get("/me", dependencies=[Depends(JWTBearer())])
async def get_user():
    return {
        "username": "test"
    }
