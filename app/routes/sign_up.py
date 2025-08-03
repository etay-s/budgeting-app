from quart import Blueprint, request
from quart_schema import validate_request, validate_response
from app.schemas.sign_up import SignUpRequest, SignUpResponse
from app.db import AsyncSessionLocal
from app.models import User
from argon2 import PasswordHasher

sign_up_bp = Blueprint('sign_up', __name__)

@sign_up_bp.post('/sign-up')
@validate_request(SignUpRequest)
@validate_response(SignUpResponse)
async def sign_up(data: SignUpRequest) -> SignUpResponse:
    ph = PasswordHasher()
    async with AsyncSessionLocal() as session:
        user = User(name=data.email, email=data.email, hashed_password=ph.hash(data.password))
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return SignUpResponse(id=user.id, name=user.name, email=user.email, password=user.hashed_password)
    