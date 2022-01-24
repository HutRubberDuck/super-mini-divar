def send_otp(phone, code):
    from src.services.sms import send_sms
    return send_sms(phone, 'Your Code is: ' + code)


def generate_otp_code(length=4):
    import random
    import string
    return ''.join(random.choice(string.digits) for i in range(length))
