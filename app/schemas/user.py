from pydantic import BaseModel, EmailStr, UUID4


class SignUpRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class SignUpResponse(BaseModel):
    id: UUID4


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
