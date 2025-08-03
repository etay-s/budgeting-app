from dataclasses import dataclass

@dataclass
class SignUpRequest:
    name: str
    email: str

@dataclass
class SignUpResponse(SignUpRequest):
    id: int