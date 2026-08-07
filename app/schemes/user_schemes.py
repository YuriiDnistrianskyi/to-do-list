from pydantic import BaseModel, EmailStr
from typing import Optional


class CreateUserScheme(BaseModel):
    name: str
    email: EmailStr
    password: str

class UpdateUserScheme(BaseModel):
    name: Optional[str] = None
