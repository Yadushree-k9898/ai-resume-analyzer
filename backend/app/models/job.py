
# from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
# from sqlalchemy.dialects.postgresql import JSON
# from sqlalchemy import func
# from sqlalchemy.orm import relationship
# from app.core.database import Base

# class Job(Base):
#     __tablename__ = "jobs"

#     id = Column(Integer, primary_key=True, index=True)
#     external_id = Column(String, unique=True, nullable=False)  # Stores the external job ID from the API
#     title = Column(String, nullable=False)
#     description = Column(Text, nullable=False)
#     skills_required = Column(JSON, nullable=False)  # Store skills in JSON format
#     company_name = Column(String, nullable=False)   # Company name from the API
#     location = Column(String, nullable=False)       # Job location (e.g., Remote, On-site, Hybrid)
#     job_type = Column(String, nullable=False)       # Employment type (e.g., Full-time, Part-time, Internship)
#     created_at = Column(DateTime(timezone=True), server_default=func.now())

#     # Define relationship with JobMatch
#     job_matches = relationship("JobMatch", back_populates="job")

#     def __repr__(self):
#         return f"<Job {self.title} at {self.company_name} ({self.location})>"


from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import func
from sqlalchemy.orm import relationship
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
    apply_link = Column(String, nullable=False)     # Job application URL
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Define relationship with JobMatch
    job_matches = relationship("JobMatch", back_populates="job")

    def __repr__(self):
        return f"<Job {self.title} at {self.company_name} ({self.location})>"
