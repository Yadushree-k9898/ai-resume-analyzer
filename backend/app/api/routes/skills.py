from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException, Request
from pydantic import BaseModel, ValidationError
from app.core.database import get_db
from app.models import Resume, Job, JobMatch

router = APIRouter()

# ✅ Define Pydantic model for the request body
class SkillsRequest(BaseModel):
    resume_id: int
    job_id: int

@router.post("/skills")
async def analyze_skills_from_db(request: Request, db: Session = Depends(get_db)):
    """Fetches resume skills and job skills from the database and finds missing skills."""
    
    try:
        # ✅ Read the incoming JSON request
        data = await request.json()
        
        if not data:
            raise HTTPException(status_code=400, detail="Request body is empty. Please provide valid JSON data.")

        print("Received Data:", data)  # Debugging log

        # ✅ Validate JSON using Pydantic
        skills_request = SkillsRequest(**data)

    except ValidationError as e:
        raise HTTPException(status_code=400, detail="Invalid request format: " + str(e))

    except Exception as e:
        raise HTTPException(status_code=400, detail="Error processing request: " + str(e))

    # ✅ Fetch resume from the database
    resume = db.query(Resume).filter(Resume.id == skills_request.resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found.")

    # ✅ Fetch job from the database
    job = db.query(Job).filter(Job.id == skills_request.job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found.")

    # ✅ Extract skills from resume & job
    resume_skills = set(resume.parsed_skills or [])  # Ensure it's a set
    job_skills = set(job.skills_required or [])  # Ensure it's a set

    # ✅ Determine missing skills
    missing_skills = job_skills - resume_skills

    # ✅ Calculate match score
    match_score = int(((len(resume_skills & job_skills)) / max(len(job_skills), 1)) * 100)  # Match percentage

    # ✅ Store job match result in the JobMatch table
    job_match = JobMatch(
        user_id=resume.user_id,
        resume_id=resume.id,
        job_id=job.id,
        match_score=match_score,
        missing_skills=",".join(missing_skills) if missing_skills else None
    )
    db.add(job_match)
    db.commit()

    # ✅ Return response
    return {
        "resume_skills": list(resume_skills),
        "job_skills": list(job_skills),
        "missing_skills": list(missing_skills),
        "match_score": match_score,
        "recommendations": "Consider learning these missing skills." if missing_skills else "You are a great match for this job!"
    }
