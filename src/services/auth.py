import time
from typing import Dict, Union, Any

import jwt
from pydantic import BaseModel, Field

from src.core.settings import JWT_SECRET_KEY, JWT_ALGORITHM


def sign_jwt(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = str(jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM))

    return {
        "access_token": token
    }


def decode_jwt(token: str) -> Union[Dict[str, Any], None]:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except jwt.ExpiredSignatureError:
        return None


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Abdulazeez Abdulazeez Adeshina",
                "email": "abdulazeez@x.com",
                "password": "weakpassword"
            }
        }


class UserLoginSchema(BaseModel):
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "abdulazeez@x.com",
                "password": "weakpassword"
            }
        }


def check_user(data: UserLoginSchema):
    # check db for user
    return True
