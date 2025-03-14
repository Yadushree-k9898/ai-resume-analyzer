# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from app.core.database import Base 

# class JobMatch(Base):
#     __tablename__ = "job_matches"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     resume_id = Column(Integer, ForeignKey("resumes.id", ondelete="CASCADE"), nullable=False)  # ✅ Ensure proper deletion
#     job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
#     match_score = Column(Integer, nullable=False)  # Match percentage (0-100)
#     missing_skills = Column(String, nullable=True)  # Comma-separated missing skills

#     user = relationship("User", back_populates="job_matches")
#     job = relationship("Job", back_populates="job_matches")
#     resume = relationship("Resume", back_populates="job_matches")  # ✅ Relationship with Resume



from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base 

class JobMatch(Base):
    __tablename__ = "job_matches"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    resume_id = Column(Integer, ForeignKey("resumes.id", ondelete="CASCADE"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    match_score = Column(Integer, nullable=False)  # Match percentage (0-100)

    user = relationship("User", back_populates="job_matches")
    job = relationship("Job", back_populates="job_matches")
    resume = relationship("Resume", back_populates="job_matches")
