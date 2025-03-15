from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Dict, Any
from app.models.dashboard import Dashboard
from app.models.user import User
from app.models.resume import Resume
from app.models.job_application import JobApplication
from app.core.database import get_db
from app.api.routes.auth import get_current_user
from sqlalchemy.sql import func

router = APIRouter()


@router.get("/dashboard", response_model=Dict[str, Any])
async def get_dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Fetch the user's dashboard data."""

    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized user")

    # Fetch dashboard entry
    dashboard = db.query(Dashboard).filter(Dashboard.user_id == current_user.id).first()

    if not dashboard:
        return {
            "dashboard": None,
            "message": "No dashboard data available. Upload a resume or apply for jobs."
        }

    return {
        "dashboard": {
            "total_resumes": dashboard.total_resumes,
            "latest_resume_id": dashboard.latest_resume_id,
            "best_resume_id": dashboard.best_resume_id,
            "resume_score": dashboard.resume_score,
            "average_resume_score": dashboard.average_resume_score,
            "total_jobs_applied": dashboard.total_jobs_applied,
            "job_application_status": dashboard.job_application_status,
            "job_matches": dashboard.job_matches,
            "total_job_matches": dashboard.total_job_matches,
            "missing_skills": dashboard.missing_skills,
            "skills_analysis": dashboard.skills_analysis,
            "last_updated": dashboard.last_updated.strftime("%Y-%m-%d %H:%M:%S"),
        },
        "message": "Dashboard fetched successfully"
    }


@router.put("/dashboard/update")
async def update_dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update dashboard data when a user uploads a resume or applies for a job."""

    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized user")

    # Fetch existing dashboard
    dashboard = db.query(Dashboard).filter(Dashboard.user_id == current_user.id).first()

    # Fetch user-related resume data
    total_resumes = db.query(Resume).filter(Resume.user_id == current_user.id).count()
    latest_resume = db.query(Resume).filter(Resume.user_id == current_user.id).order_by(Resume.created_at.desc()).first()
    best_resume = db.query(Resume).filter(Resume.user_id == current_user.id).order_by(Resume.score.desc()).first()

    # Fetch job application data
    total_jobs_applied = db.query(JobApplication).filter(JobApplication.user_id == current_user.id).count()
    job_statuses = db.query(JobApplication.status, func.count()).filter(JobApplication.user_id == current_user.id).group_by(JobApplication.status).all()
    job_application_status = {status: count for status, count in job_statuses}

    # Ensure default values for job application status
    default_statuses = {"Applied": 0, "Interview": 0, "Rejected": 0, "Hired": 0}
    job_application_status = {**default_statuses, **job_application_status}

    if not dashboard:
        # Create a new dashboard entry if it doesn't exist
        dashboard = Dashboard(
            user_id=current_user.id,
            total_resumes=total_resumes,
            latest_resume_id=latest_resume.id if latest_resume else None,
            best_resume_id=best_resume.id if best_resume else None,
            resume_score=latest_resume.score if latest_resume else 0,
            average_resume_score=db.query(func.avg(Resume.score)).filter(Resume.user_id == current_user.id).scalar() or 0,
            total_jobs_applied=total_jobs_applied,
            job_application_status=job_application_status,
            job_matches=[],
            total_job_matches=0,
            missing_skills=[],
            skills_analysis={},
            last_updated=datetime.utcnow()
        )
        db.add(dashboard)
    else:
        # Update existing dashboard
        dashboard.total_resumes = total_resumes
        dashboard.latest_resume_id = latest_resume.id if latest_resume else None
        dashboard.best_resume_id = best_resume.id if best_resume else None
        dashboard.resume_score = latest_resume.score if latest_resume else 0
        dashboard.average_resume_score = db.query(func.avg(Resume.score)).filter(Resume.user_id == current_user.id).scalar() or 0
        dashboard.total_jobs_applied = total_jobs_applied
        dashboard.job_application_status = job_application_status
        dashboard.last_updated = datetime.utcnow()

    db.commit()

    return {"message": "Dashboard updated successfully"}


@router.delete("/dashboard")
async def delete_dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete the dashboard data for a user."""

    dashboard = db.query(Dashboard).filter(Dashboard.user_id == current_user.id).first()

    if not dashboard:
        raise HTTPException(status_code=404, detail="Dashboard not found")

    db.delete(dashboard)
    db.commit()

    return {"message": "Dashboard deleted successfully"}
