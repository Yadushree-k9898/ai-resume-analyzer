
# from sqlalchemy import Column, Integer, String, Text
# from sqlalchemy.orm import relationship
# from app.core.database import Base  # Ensure this path is correct
# from app.models.job_match import JobMatch  # Ensure this import is present


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True, nullable=False)  # Ensure username is required
#     full_name = Column(String, nullable=False)
#     email = Column(String, unique=True, index=True, nullable=False)  # Indexed for fast lookups
#     hashed_password = Column(String, nullable=False)
#     phone_number = Column(String, nullable=True, index=True)  # Optional but indexed for efficiency

#     job_title = Column(String, nullable=True)  
#     industry = Column(String, nullable=True)
#     skills = Column(Text, nullable=True)  # Store skills as a comma-separated string or JSON
#     experience_level = Column(String, nullable=True)
#     location = Column(String, nullable=True)
#     linkedin_url = Column(String, nullable=True)
#     portfolio_url = Column(String, nullable=True)
    
#     role = Column(String, default="user", nullable=False)  # Ensure role is always present

#     # Relationships
#     job_applications = relationship("JobApplication", back_populates="user", cascade="all, delete-orphan", lazy="selectin")
#     resumes = relationship("Resume", back_populates="user", cascade="all, delete-orphan", lazy="selectin")
#     job_matches = relationship("JobMatch", back_populates="user")




from sqlalchemy import Column, String, Integer
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)  # ✅ Can be NULL
    role = Column(String, default="user")

    # Extra Fields (Users Can Add Later)
    username = Column(String, nullable=True)
    job_title = Column(String, nullable=True)
    industry = Column(String, nullable=True)
    skills = Column(String, nullable=True)
    experience_level = Column(String, nullable=True)
    location = Column(String, nullable=True)
    linkedin_url = Column(String, nullable=True)
    portfolio_url = Column(String, nullable=True)
