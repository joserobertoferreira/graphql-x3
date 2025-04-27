from datetime import datetime, timedelta
from typing import Optional

import jwt

from app.core.settings import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY


class JWTManager:
    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(minutes=float(ACCESS_TOKEN_EXPIRE_MINUTES))

        to_encode.update({'exp': expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def verify_token(token: str) -> bool:
        try:
            decode_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            current_timestamp = datetime.now().timestamp()

            if not decode_token:
                raise ValueError('Token is invalid')
            elif decode_token['exp'] <= current_timestamp:
                raise ValueError('Token has expired')

            return True
        except ValueError:
            return False
