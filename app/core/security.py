from passlib.context import CryptContext
import hashlib

pwd_context = CryptContext(
    schemes=['argon2'],
    deprecated='auto'
)


def create_hash(password: str) -> str:
    hashed = pwd_context.hash(password)
    return hashed

def verify_password(password_hash: str, password: str) -> bool:
    return pwd_context.verify(password, password_hash)
