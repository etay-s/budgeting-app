from quart import jsonify
from app.db import AsyncSessionLocal
from app.models import User
from app.auth import hash_password, verify_password, create_access_token
from app.repositories.user_repo import get_user_by_email
from sqlalchemy.exc import IntegrityError


async def register_user(name: str, email: str, password: str) -> str:
    async with AsyncSessionLocal() as session:
        try:
            user = User(name=name, email=email, hashed_password=hash_password(password))
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user.id
        except IntegrityError as e:
            await session.rollback()
            raise ValueError("Email already registered") from e


async def login_user(email: str, password: str) -> str:
    async with AsyncSessionLocal() as session:
        user = await get_user_by_email(session, email)

        if not user or not verify_password(password, user.hashed_password):
            raise ValueError("Invalid credentials")

        token = create_access_token({"sub": str(user.id), "email": user.email})

        return token
