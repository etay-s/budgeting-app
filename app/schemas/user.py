from pydantic import BaseModel


class SignUpRequest(BaseModel):
    name: str
    email: str
    password: str


class SignUpResponse(BaseModel):
    id: str


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
