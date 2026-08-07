from fastapi import HTTPException, status
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

from app.core.config import SECRET_JWT_KEY


def create_access_token(user_id: int):
    expire = datetime.now(timezone.utc) + timedelta(minutes=5)

    encode = {
        'user_id': user_id,
        'exp': expire
    }

    return jwt.encode(encode, SECRET_JWT_KEY, algorithm='HS256')

def create_refresh_token(user_id: int):
    expire = datetime.now(timezone.utc) + timedelta(days=5)

    encode = {
        'user_id': user_id,
        'exp': expire
    }

    return jwt.encode(encode, SECRET_JWT_KEY, algorithm='HS256')

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_JWT_KEY, algorithms=['HS256'])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Signature expired'
        )
