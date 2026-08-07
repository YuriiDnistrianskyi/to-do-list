from pydantic import BaseModel, EmailStr
from typing import Optional


class CreateUserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

class UpdateUserSchema(BaseModel):
    name: Optional[str] = None
