from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import func
from app.core.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String, unique=True, nullable=False)  # Stores the external job ID from the API
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    skills_required = Column(JSON, nullable=False)  # Store skills in JSON format
    company_name = Column(String, nullable=False)   # Company name from the API
    location = Column(String, nullable=False)       # Job location (e.g., Remote, On-site, Hybrid)
    job_type = Column(String, nullable=False)       # Employment type (e.g., Full-time, Part-time, Internship)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Job {self.title} at {self.company_name} ({self.location})>"
