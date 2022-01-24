from fastapi import APIRouter, Body, Depends
from pydantic import BaseModel

from src.core.auth.bearer import JWTBearer
from src.core.auth.token import sign_jwt
from src.schemas.user import UserLoginSchema, UserSchema
from src.services.otp import generate_otp_code, send_otp

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


class User(BaseModel):
    username: str
    password: str


@router.post("/signup")
async def create_user(user: UserSchema = Body(...)):
    # connect to db
    return sign_jwt(user.email)


@router.post("/login")
async def user_login(user: UserLoginSchema = Body(...)):
    def check_user(data: UserLoginSchema):
        # connect to db
        return True

    if check_user(user):
        return sign_jwt(user.email)
    return {
        "error": "Wrong login details!"
    }


@router.get("/me", dependencies=[Depends(JWTBearer())])
async def get_user():
    # connect to db
    return {
        "username": "test"
    }


@router.get("/me/send_sms", dependencies=[Depends(JWTBearer())])
def send_sms():
    try:
        send_otp('9378766339', generate_otp_code())
        return {
            "message": "SMS sent!"
        }
    except Exception as e:
        print(e)
        return {
            "error": "Could not send sms please try again later!"
        }
