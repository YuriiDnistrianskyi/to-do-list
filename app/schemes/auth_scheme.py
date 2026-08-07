from pydantic import BaseModel, EmailStr

class LoginScheme(BaseModel):
    email: EmailStr
    password: str

class RefreshScheme(BaseModel):
    refresh_token: str
