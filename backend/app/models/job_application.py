from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, func
from sqlalchemy.orm import relationship
from app.core.database import Base  # Adjusted the import path

class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    status = Column(String, default="pending")  # e.g., pending, accepted, rejected
    applied_at = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship("User", back_populates="job_applications")
    job = relationship("Job")
