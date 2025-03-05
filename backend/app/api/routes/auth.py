from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import (
    hash_password, verify_password, create_access_token, verify_token
)
from app.models.user import User
from pydantic import BaseModel, EmailStr, validator
from datetime import timedelta
from fastapi.security import OAuth2PasswordBearer
import re

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# ✅ User Create Schema
class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    phone_number: str | None = None
    username: str | None = None
    job_title: str | None = None
    industry: str | None = None
    skills: str | None = None
    experience_level: str | None = None
    location: str | None = None
    linkedin_url: str | None = None
    portfolio_url: str | None = None

    @validator("password")
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return v

    @validator("phone_number")
    def valid_phone_number(cls, v):
        if v and not re.match(r'^\+?1?\d{9,15}$', v):
            raise ValueError("Phone number must be in a valid format")
        return v


# ✅ Separate Schema for Login (Fix)
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# ✅ Update Schema
class UserUpdate(BaseModel):
    email: EmailStr | None = None
    password: str | None = None
    full_name: str | None = None
    phone_number: str | None = None
    username: str | None = None
    job_title: str | None = None
    industry: str | None = None
    skills: str | None = None
    experience_level: str | None = None
    location: str | None = None
    linkedin_url: str | None = None
    portfolio_url: str | None = None


ACCESS_TOKEN_EXPIRE_HOURS = 1

# ✅ Register Route
@router.post("/register/", status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)
    db_user = User(
        full_name=user.full_name,
        email=user.email,
        hashed_password=hashed_password,
        phone_number=user.phone_number,
        username=user.username,
        job_title=user.job_title,
        industry=user.industry,
        skills=user.skills,
        experience_level=user.experience_level,
        location=user.location,
        linkedin_url=user.linkedin_url,
        portfolio_url=user.portfolio_url,
        role="user"  # Default role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User registered successfully"}

# ✅ Login Route (Fix)
@router.post("/login/")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token(
        {"sub": db_user.email, "role": db_user.role},
        expires_delta=timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    )
    return {"access_token": access_token, "token_type": "bearer"}

# ✅ Get Current User (Fix)
@router.get("/me/")
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_data = verify_token(token)
    if not user_data["valid"]:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=user_data["message"])

    user_email = user_data["payload"].get("sub")
    db_user = db.query(User).filter(User.email == user_email).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return {"id": db_user.id, "email": db_user.email, "full_name": db_user.full_name}

# ✅ Get All Users (Fix Admin Check)
@router.get("/users/")
def get_all_users(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user_data = verify_token(token)
    if not user_data["valid"]:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=user_data["message"])
    
    if user_data["payload"].get("role") != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not authorized to access this resource")

    users = db.query(User).all()
    return [{"id": user.id, "email": user.email, "full_name": user.full_name} for user in users]

# ✅ Update User (Fix)
@router.put("/update/")
def update_user(user_update: UserUpdate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user_data = verify_token(token)
    if not user_data["valid"]:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=user_data["message"])

    user_email = user_data["payload"].get("sub")
    db_user = db.query(User).filter(User.email == user_email).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    for field, value in user_update.dict(exclude_unset=True).items():
        setattr(db_user, field, value)

    if user_update.password:
        db_user.hashed_password = hash_password(user_update.password)

    db.commit()
    db.refresh(db_user)
    return {"message": "User updated successfully"}

# ✅ Delete User (Fix)
@router.delete("/delete/")
def delete_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user_data = verify_token(token)
    if not user_data["valid"]:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=user_data["message"])

    user_email = user_data["payload"].get("sub")
    db_user = db.query(User).filter(User.email == user_email).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}
