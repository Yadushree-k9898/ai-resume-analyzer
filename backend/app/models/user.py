from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.core.database import Base  # Ensure this path is correct

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)  # Ensure username is required
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)  # Indexed for fast lookups
    hashed_password = Column(String, nullable=False)
    phone_number = Column(String, nullable=True, index=True)  # Optional but indexed for efficiency

    job_title = Column(String, nullable=True)  
    industry = Column(String, nullable=True)
    skills = Column(Text, nullable=True)  # Store skills as a comma-separated string or JSON
    experience_level = Column(String, nullable=True)
    location = Column(String, nullable=True)
    linkedin_url = Column(String, nullable=True)
    portfolio_url = Column(String, nullable=True)
    
    role = Column(String, default="user", nullable=False)  # Ensure role is always present

    # Relationships
    job_applications = relationship("JobApplication", back_populates="user", cascade="all, delete-orphan")
    resumes = relationship("Resume", back_populates="user", cascade="all, delete-orphan")
