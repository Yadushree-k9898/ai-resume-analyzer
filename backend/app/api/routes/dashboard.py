from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.resume import Resume

router = APIRouter()

@router.get("/dashboard")
def get_dashboard(user_id: int, db: Session = Depends(get_db)):
    resumes = db.query(Resume).filter(Resume.user_id == user_id).all()
    return {"resumes": [resume.content for resume in resumes]}
