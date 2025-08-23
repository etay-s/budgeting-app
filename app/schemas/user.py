from typing import Annotated
from pydantic import BaseModel, EmailStr, UUID4, StringConstraints
from .utils.validator_types import StrongPassword


class SignUpRequest(BaseModel):
    name: Annotated[str, StringConstraints(min_length=2, max_length=50)]
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
