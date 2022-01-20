import time
from typing import Dict, Any, Union

import jwt

from src.core.settings import JWT_SECRET_KEY, JWT_ALGORITHM


def sign_jwt(user_id: str) -> Dict[str, bytes]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

    return {
        "access_token": token
    }


def decode_jwt(token: str) -> Union[Dict[str, Any], None]:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except jwt.ExpiredSignatureError:
        return None
