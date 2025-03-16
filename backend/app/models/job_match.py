# job_match.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
# Avoid circular import by using import within the relationship function
# from app.models.user import User
from app.models.resume import Resume
from app.models.job import Job

class JobMatch(Base):
    __tablename__ = "job_matches"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    resume_id = Column(Integer, ForeignKey("resumes.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    match_score = Column(Integer, nullable=False)  # Match percentage (0-100)
    missing_skills = Column(String, nullable=True)  # Comma-separated missing skills

    # Lazy imports to prevent circular import errors
    user = relationship("User", back_populates="job_matches")  # JobMatch to User relationship
    job = relationship("Job", back_populates="job_matches")  # JobMatch to Job relationship
    resume = relationship("Resume", back_populates="job_matches")  # JobMatch to Resume relationship
