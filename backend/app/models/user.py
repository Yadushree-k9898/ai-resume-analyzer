
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.core.database import Base  # Ensure this import path is correct


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)

    job_title = Column(String, nullable=True)  # Ensure this exists
    industry = Column(String, nullable=True)
    skills = Column(Text, nullable=True)
    experience_level = Column(String, nullable=True)
    location = Column(String, nullable=True)
    linkedin_url = Column(String, nullable=True)
    portfolio_url = Column(String, nullable=True)
    role = Column(String, default="user")
    job_applications = relationship("JobApplication", back_populates="user")
    resumes = relationship("Resume", back_populates="user")  
