from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.core.config import settings  # Make sure settings are properly imported

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hashes a password using bcrypt."""
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    """Verifies that a plain password matches the hashed password."""
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = timedelta(hours=2)):
    """
    Creates a JWT access token with an expiration time.
    
    :param data: Payload data for the token (must contain 'sub' key)
    :param expires_delta: Time duration after which the token expires (default: 2 hours)
    :return: Encoded JWT token
    """
    to_encode = data.copy()

    # Ensure 'sub' (subject) is included in the payload, which is usually the user's identifier
    if "sub" not in to_encode:
        raise ValueError("Missing 'sub' in token payload")  

    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    """
    Verifies a JWT token and checks its expiration.
    
    :param token: JWT token to be verified
    :return: Dictionary with validation result and payload (if valid)
    """
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        
        # Check for expiration time in the payload
        exp = payload.get("exp")
        if exp:
            expiration_time = datetime.fromtimestamp(exp, timezone.utc)
            # If the current time is past the expiration time, the token is invalid
            if datetime.now(timezone.utc) > expiration_time:
                return {"valid": False, "message": "Token has expired"}

        # Return valid token with payload
        return {"valid": True, "payload": payload}

    except JWTError as e:
        # More descriptive error handling for invalid tokens
        print(f"Error decoding token: {e}")
        return {"valid": False, "message": "Invalid token", "error": str(e)}

