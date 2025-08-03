from dataclasses import dataclass

@dataclass
class SignUpRequest:
    name: str
    email: str
    password: str

@dataclass
class SignUpResponse(SignUpRequest):
    id: str

@dataclass
class LoginRequest:
    email: str
    password: str

@dataclass
class LoginResponse:
    access_token: str
    token_type: str = 'bearer'