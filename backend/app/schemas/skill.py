from pydantic import BaseModel
from typing import Optional

class SkillBase(BaseModel):
    name: str
    category: Optional[str] = None
    skill_type: Optional[str] = None

class SkillCreate(SkillBase):
    user_id: int
    resume_id: int

class SkillResponse(SkillBase):
    id: int

    class Config:
        orm_mode = True
