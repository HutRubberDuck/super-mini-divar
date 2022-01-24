from datetime import datetime

from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session

from src.core.auth.token import sign_jwt
from src.core.database import database
from src.model import Phone
from src.schemas.user import UserLoginOTPSchema, UserLoginOTPConfirmSchema
from src.services.otp import generate_otp_code, send_otp

router = APIRouter(
    prefix="/otp",
    tags=["otp"],
)


@router.post("/login/code")
async def user_request_user_otp(user: UserLoginOTPSchema = Body(...), db: Session = Depends(database.get_session)):
    try:
        otp_code = generate_otp_code()
        send_otp(user.phone, otp_code)
        db.query(Phone).filter(Phone.number == user.phone, Phone.is_verified == False).delete()
        Phone(number=user.phone, otp=otp_code)
        db.add(Phone(number=user.phone, otp=otp_code))
        db.commit()
        return {
            "message": "OTP sent!"
        }
    except Exception as e:
        print(e)
        return {
            "error": "Could not send sms please try again later!"
        }


@router.post("/login")
async def user_login(user: UserLoginOTPConfirmSchema = Body(...), db: Session = Depends(database.get_session)):
    phone_db = db.query(Phone).filter(Phone.number == user.phone, Phone.is_verified == False).first()
    if phone_db and phone_db.otp == user.code:
        db.query(Phone).filter(Phone.number == user.phone, Phone.otp != user.code).delete()
        phone_db.is_verified = True
        phone_db.verified_at = datetime.now()
        db.add(phone_db)
        db.commit()
        return sign_jwt(user.phone)
    return {"error": "Wrong OTP!"}
