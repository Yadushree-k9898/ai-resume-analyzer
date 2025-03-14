# from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, func, JSON
# from sqlalchemy.orm import relationship
# from app.core.database import Base

# class Resume(Base):
#     __tablename__ = "resumes"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
#     file_path = Column(String, nullable=False, index=True)  # Indexed for faster queries
#     extracted_text = Column(Text, nullable=True)  # Stores parsed resume text
#     score = Column(Integer, nullable=True)  # AI-generated resume score
#     parsed_skills = Column(JSON, nullable=True)  # Extracted skills in JSON format
#     job_matches = Column(JSON, nullable=True)  # Suggested job matches
#     improvement_suggestions = Column(Text, nullable=True)  # Resume improvement feedback
#     created_at = Column(DateTime(timezone=True), server_default=func.now())


#     user = relationship("User", back_populates="resumes", lazy="select")


# from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, func, JSON
# from sqlalchemy.orm import relationship
# from sqlalchemy.dialects.postgresql import JSONB
# from app.core.database import Base

# class Resume(Base):
#     __tablename__ = "resumes"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
#     file_path = Column(String, nullable=False, index=True)
#     extracted_text = Column(Text, nullable=True)
#     score = Column(Integer, nullable=True)
#     parsed_skills = Column(JSONB, nullable=True)  # ✅ Store parsed skills as JSON
#     missing_skills = Column(JSONB, nullable=True)  # ✅ Store missing skills as JSON
#     improvement_suggestions = Column(Text, nullable=True)
#     created_at = Column(DateTime(timezone=True), server_default=func.now())

#     job_matches = relationship("JobMatch", back_populates="resume", cascade="all, delete-orphan")
#     user = relationship("User", back_populates="resumes", lazy="selectin")



from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.core.database import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    file_path = Column(String, nullable=False, index=True)
    extracted_text = Column(Text, nullable=True)
    score = Column(Integer, nullable=True)
    skills = Column(JSONB, nullable=True)  # ✅ Store parsed skills as JSON
    missing_skills = Column(JSONB, nullable=True)  # ✅ Store missing skills as JSON
    improvement_suggestions = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    job_matches = relationship("JobMatch", back_populates="resume", cascade="all, delete-orphan")
    user = relationship("User", back_populates="resumes", lazy="selectin")
