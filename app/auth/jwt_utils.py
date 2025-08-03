import jwt 
from datetime import datetime, timezone, timedelta
from app.config import settings
from functools import wraps
from quart import request

def create_access_token(data: dict, expires_delta: int = 3600):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(seconds=expires_delta)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.jwt_secret, algorithm="HS256")

def verify_token(token: str):
    try:
        return jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    
def jwt_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        token = auth_header.replace("Bearer ", "")
        payload = verify_token(token)
        if not payload:
            return {"error": "Unauthorized"}, 401

        return await func(*args, **kwargs)

    return wrapper