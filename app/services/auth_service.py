from app.db import AsyncSessionLocal
from app.models import User
from app.auth import hash_password, verify_password, create_access_token
from sqlalchemy.exc import IntegrityError
from app.repositories.user_repo import create_user, get_user_by_email


async def register_user(name: str, email: str, password: str) -> str:
    async with AsyncSessionLocal():
        try:
            user = User(name=name, email=email, hashed_password=hash_password(password))
            await create_user(user)
            return user.id
        except IntegrityError as e:
            raise ValueError("Email already registered") from e


async def login_user(email: str, password: str) -> str:
    user = await get_user_by_email(email)

    if not user or not verify_password(password, user.hashed_password):
        raise ValueError("Invalid credentials")

    token = create_access_token({"sub": str(user.id), "email": user.email})

    return token
