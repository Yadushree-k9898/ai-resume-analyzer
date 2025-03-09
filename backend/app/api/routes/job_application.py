# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.core.database import get_db
# from app.models.job_application import JobApplication
# from app.models.job import Job
# from app.api.routes.auth import get_current_user
# import urllib.parse  # ✅ Added to decode job ID

# router = APIRouter(prefix="/api/job_applications", tags=["Job Applications"])

# @router.post("/apply/{job_id}", status_code=201)
# def apply_for_job(job_id: str, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
#     """
#     Apply for a job using the job ID with authentication.
#     """
#     if not current_user:
#         raise HTTPException(status_code=401, detail="Authentication required")

#     user_id = current_user.get("id")
#     if not user_id:
#         raise HTTPException(status_code=401, detail="Invalid authentication token")

#     # ✅ Decode job_id (fix for URL encoding issues)
#     job_id = urllib.parse.unquote(job_id)

#     # ✅ Check if job exists
#     job = db.query(Job).filter(Job.id == job_id).first()
#     if not job:
#         raise HTTPException(status_code=404, detail="Job not found")

#     # ✅ Check if the user has already applied
#     existing_application = db.query(JobApplication).filter(
#         JobApplication.user_id == user_id, JobApplication.job_id == job_id
#     ).first()

#     if existing_application:
#         raise HTTPException(status_code=400, detail="You have already applied for this job")

#     # ✅ Apply for the job
#     job_application = JobApplication(user_id=user_id, job_id=job_id)
#     db.add(job_application)
#     db.commit()
#     db.refresh(job_application)

#     return {"message": "✅ Successfully applied for the job!", "job_id": job_id}

# @router.get("/applied_jobs/")
# def get_applied_jobs(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
#     """
#     Fetch all jobs a user has applied for with authentication.
#     """
#     if not current_user:
#         raise HTTPException(status_code=401, detail="Authentication required")

#     user_id = current_user.get("id")
#     if not user_id:
#         raise HTTPException(status_code=401, detail="Invalid authentication token")

#     applications = db.query(JobApplication).filter(JobApplication.user_id == user_id).all()

#     if not applications:
#         return {"message": "No job applications found"}

#     applied_jobs = []
#     for app in applications:
#         job = db.query(Job).filter(Job.id == app.job_id).first()
#         if job:
#             applied_jobs.append({
#                 "job_id": str(job.id),
#                 "title": job.title,
#                 "description": job.description,
#                 "skills_required": job.skills_required,
#                 "status": app.status,
#                 "applied_at": app.applied_at
#             })

#     return {"applied_jobs": applied_jobs}


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.job_application import JobApplication
from app.models.job import Job
from app.api.routes.auth import get_current_user
import urllib.parse  # ✅ Added to decode job ID

router = APIRouter(prefix="/api/job_applications", tags=["Job Applications"])

@router.post("/apply/{job_id}", status_code=201)
def apply_for_job(job_id: str, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """
    Apply for a job using the job ID with authentication.
    """
    if not current_user:
        raise HTTPException(status_code=401, detail="Authentication required")

    user_id = current_user.get("id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid authentication token")

    # ✅ Decode job_id (fix for URL encoding issues)
    job_id = urllib.parse.unquote(job_id)

    # ✅ Check if job exists
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    # ✅ Check if the user has already applied
    existing_application = db.query(JobApplication).filter(
        JobApplication.user_id == user_id, JobApplication.job_id == job_id
    ).first()

    if existing_application:
        raise HTTPException(status_code=400, detail="You have already applied for this job")

    # ✅ Apply for the job
    job_application = JobApplication(user_id=user_id, job_id=job_id)
    db.add(job_application)
    db.commit()
    db.refresh(job_application)

    return {"message": "✅ Successfully applied for the job!", "job_id": job_id}

@router.get("/applied_jobs/")
def get_applied_jobs(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """
    Fetch all jobs a user has applied for with authentication.
    """
    if not current_user:
        raise HTTPException(status_code=401, detail="Authentication required")

    user_id = current_user.get("id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid authentication token")

    applications = db.query(JobApplication).filter(JobApplication.user_id == user_id).all()

    if not applications:
        return {"message": "No job applications found"}

    applied_jobs = []
    for app in applications:
        job = db.query(Job).filter(Job.id == app.job_id).first()
        if job:
            applied_jobs.append({
                "job_id": str(job.id),
                "title": job.title,
                "description": job.description,
                "skills_required": job.skills_required,
                "status": app.status,
                "applied_at": app.applied_at
            })

    return {"applied_jobs": applied_jobs}
