from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import func
from app.core.database import Base
from app.api.routes import auth, resume


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    file_path = Column(String, nullable=False)
    extracted_text = Column(Text, nullable=True)
    resume_score = Column(Integer, nullable=True)  # AI-based score
    parsed_skills = Column(JSON, nullable=True)  # Extracted skills in JSON format
    job_matches = Column(JSON, nullable=True)  # List of matched jobs
    improvement_suggestions = Column(Text, nullable=True)  # Resume improvement tips
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship("User", back_populates="resumes")
