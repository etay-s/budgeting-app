from quart import Blueprint, request, jsonify
from quart_schema import validate_request, validate_response
from app.schemas.user import SignUpRequest, SignUpResponse, LoginRequest, LoginResponse
from app.db import AsyncSessionLocal
from app.models import User
from app.auth.password_utils import hash_password, verify_password
from app.auth.jwt_utils import create_access_token
from app.repositories.user_repo import get_user_by_email

sign_up_bp = Blueprint('sign_up', __name__)
login_bp = Blueprint('login', __name__)

@sign_up_bp.post('/sign-up')
@validate_request(SignUpRequest)
@validate_response(SignUpResponse)
async def sign_up(data: SignUpRequest) -> SignUpResponse:
    async with AsyncSessionLocal() as session:
        user = User(
            name=data.email, 
            email=data.email, 
            hashed_password=hash_password(data.password)
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return SignUpResponse(id=user.id, name=user.name, email=user.email, password=user.hashed_password)
    
@login_bp.post('/login')
@validate_request(LoginRequest)
@validate_response(LoginResponse)
async def login(data: LoginRequest):
    async with AsyncSessionLocal() as session:
        user = await get_user_by_email(session, data.email)

        if not user or not verify_password(data.password, user.hashed_password):
            return jsonify({"error": "Invalid credentials"}), 401
        
        token = create_access_token({"sub": str(user.id), "email": user.email})
        return LoginResponse(access_token=token)