from quart import Blueprint, request
from quart_schema import validate_request, validate_response
from schemas.sign_up import SignUpRequest, SignUpResponse
from db import AsyncSessionLocal
from models import User

sign_up_bp = Blueprint('sign_up', __name__)

@sign_up_bp.post('/sign-up')
@validate_request(SignUpRequest)
@validate_response(SignUpResponse)
async def balance(data: SignUpRequest) -> SignUpResponse:
    async with AsyncSessionLocal() as session:
        user = User(name=data["name"], email=data["email"])
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return SignUpResponse(id=user.id, name=user.name, email=user.email)
    