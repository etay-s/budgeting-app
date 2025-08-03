from dataclasses import dataclass

@dataclass
class SignUpRequest:
    name: str
    email: str
    password: str

@dataclass
class SignUpResponse(SignUpRequest):
    id: str