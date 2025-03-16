# user.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.core.database import Base  # Ensure this path is correct
from app.models.job_match import JobMatch  # Import here for the relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    phone_number = Column(String, nullable=True, index=True)

    job_title = Column(String, nullable=True)
    industry = Column(String, nullable=True)
    skills = Column(Text, nullable=True)
    experience_level = Column(String, nullable=True)
    location = Column(String, nullable=True)
    linkedin_url = Column(String, nullable=True)
    portfolio_url = Column(String, nullable=True)
    
    role = Column(String, default="user", nullable=False)

    # Relationships
    job_applications = relationship("JobApplication", back_populates="user", cascade="all, delete-orphan")
    resumes = relationship("Resume", back_populates="user", cascade="all, delete-orphan")
    job_matches = relationship("JobMatch", back_populates="user")  # JobMatch relationship
