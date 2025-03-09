from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = timedelta(hours=2)):
    to_encode = data.copy()

    # Ensure 'sub' (subject) is included in the payload, which is usually the user's identifier
    if "sub" not in to_encode:
        raise ValueError("Missing 'sub' in token payload")  

    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        exp = payload.get("exp")

        if exp:
            expiration_time = datetime.fromtimestamp(exp, timezone.utc)
            if datetime.now(timezone.utc) > expiration_time:
                return {"valid": False, "message": "Token has expired"}

        return {"valid": True, "payload": payload}

    except JWTError as e:
        print(f"Error decoding token: {e}")
        return {"valid": False, "message": "Invalid token", "error": str(e)}
