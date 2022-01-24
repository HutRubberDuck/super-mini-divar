from kavenegar import KavenegarAPI, APIException, HTTPException

from src.core.settings import OTP_API_KEY


def send_sms(phone, message):
    try:
        api = KavenegarAPI(OTP_API_KEY)
        response = api.sms_send({
            'sender': '100047778',
            'receptor': phone,
            'message': message,
        })
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
