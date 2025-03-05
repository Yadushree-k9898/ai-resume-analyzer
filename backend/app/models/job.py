from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import func
from app.core.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    skills_required = Column(JSON, nullable=False)  # Store skills in JSON format
    created_at = Column(DateTime(timezone=True), server_default=func.now())
