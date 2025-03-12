from sqlalchemy import Column, Integer, ForeignKey, JSON, Float, DateTime, func
from sqlalchemy.orm import relationship
from app.core.database import Base  # Make sure Base is imported correctly

class Dashboard(Base):
    __tablename__ = "dashboard"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    total_resumes = Column(Integer, default=0)
    latest_resume_id = Column(Integer, ForeignKey("resumes.id"), nullable=True)
    best_resume_id = Column(Integer, ForeignKey("resumes.id"), nullable=True)
    resume_score = Column(Integer, default=0)
    average_resume_score = Column(Float, default=0.0)
    total_jobs_applied = Column(Integer, default=0)
    job_application_status = Column(JSON, default={})
    job_matches = Column(JSON, default=[])
    total_job_matches = Column(Integer, default=0)
    missing_skills = Column(JSON, default=[])
    skills_analysis = Column(JSON, default={})
    created_at = Column(DateTime, server_default=func.now())
    last_updated = Column(DateTime, server_default=func.now(), onupdate=func.now())
