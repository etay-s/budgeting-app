from pydantic import BaseModel

class SignUpRequest(BaseModel):
    name: str
    email: str
    password: str

class SignUpResponse(SignUpRequest):
    id: str

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'