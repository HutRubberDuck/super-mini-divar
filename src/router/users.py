from fastapi import APIRouter, Body, Depends

from src.core.auth.bearer import JWTBearer
from src.core.auth.token import sign_jwt
from src.schemas.user import UserSchema, UserLoginSchema

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/signup")
async def create_user(user: UserSchema = Body(...)):
    # TODO: connect to db
    return sign_jwt(user.email)


@router.post("/login")
async def user_login(user: UserLoginSchema = Body(...)):
    def check_user(data: UserLoginSchema):
        # TODO: connect to db
        return True

    if check_user(user):
        return sign_jwt(user.phone)
    return {
        "error": "Wrong login details!"
    }


@router.get("/me", dependencies=[Depends(JWTBearer())])
async def get_user():
    # TODO: get user from db and return it
    return {
        "username": "test"
    }
