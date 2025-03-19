from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=True)  # E.g., Programming, Database, Soft Skill
    skill_type = Column(String, nullable=True)  # Technical, Soft, etc.
    
    user_id = Column(Integer, ForeignKey("users.id"))
    resume_id = Column(Integer, ForeignKey("resumes.id"))

    user = relationship("User", back_populates="skills")
    resume = relationship("Resume", back_populates="skills")

# Add relationships in user.py and resume.py:
# User model: skills = relationship("Skill", back_populates="user")
# Resume model: skills = relationship("Skill", back_populates="resume")
