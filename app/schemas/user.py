from pydantic import BaseModel, EmailStr, UUID4
from .utils.validator_types import StrongPassword, Name


class SignUpRequest(BaseModel):
    name: Name
    email: EmailStr
    password: StrongPassword


class SignUpResponse(BaseModel):
    id: UUID4


class LoginRequest(BaseModel):
    email: EmailStr
    password: StrongPassword


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
