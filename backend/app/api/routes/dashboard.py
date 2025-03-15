from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Dict, Any, List

from app.models.dashboard import Dashboard
from app.models.user import User
from app.models.resume import Resume
from app.models.job_application import JobApplication
from app.models.job import Job
from app.models.job_match import JobMatch
from app.core.database import get_db
from app.api.routes.auth import get_current_user
from sqlalchemy.sql import func

router = APIRouter()

# -----------------------------------------------
# 📌 Get Dashboard Data
# -----------------------------------------------
@router.get("/dashboard", response_model=Dict[str, Any])
async def get_dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Fetch the user's dashboard data."""

    dashboard = db.query(Dashboard).filter(Dashboard.user_id == current_user.id).first()

    if not dashboard:
        return {
            "dashboard": None,
            "message": "No dashboard data available. Upload a resume or apply for jobs."
        }

    # Retrieve job matches from both Dashboard JSON field & JobMatch table
    job_matches = dashboard.job_matches if dashboard.job_matches else []
    db_job_matches = [
        {"job_id": match.job_id, "match_score": match.match_score}
        for match in db.query(JobMatch).filter_by(user_id=current_user.id).all()
    ]

    # Merge stored and computed matches (avoid duplicates)
    job_matches.extend(db_job_matches)
    job_matches = list({match["job_id"]: match for match in job_matches}.values())  # Remove duplicates

    return {
        "dashboard": {
            "total_resumes": dashboard.total_resumes,
            "latest_resume_id": dashboard.latest_resume_id,
            "best_resume_id": dashboard.best_resume_id,
            "resume_score": dashboard.resume_score,
            "average_resume_score": dashboard.average_resume_score,
            "total_jobs_applied": dashboard.total_jobs_applied,
            "job_application_status": dashboard.job_application_status or {},
            "job_matches": job_matches,
            "total_job_matches": len(job_matches),
            "last_updated": dashboard.last_updated.strftime("%Y-%m-%d %H:%M:%S"),
        },
        "message": "Dashboard fetched successfully"
    }

# -----------------------------------------------
# 📌 Update Dashboard After Resume Upload or Job Application
# -----------------------------------------------
@router.put("/dashboard/update")
async def update_dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update dashboard data when a user uploads a resume or applies for a job."""

    dashboard = db.query(Dashboard).filter(Dashboard.user_id == current_user.id).first()

    # Fetch user-related resume data
    total_resumes = db.query(Resume).filter(Resume.user_id == current_user.id).count()
    latest_resume = db.query(Resume).filter(Resume.user_id == current_user.id).order_by(Resume.created_at.desc()).first()
    best_resume = db.query(Resume).filter(Resume.user_id == current_user.id).order_by(Resume.score.desc()).first()

    # Fetch job application data
    total_jobs_applied = db.query(JobApplication).filter(JobApplication.user_id == current_user.id).count()
    job_statuses = db.query(JobApplication.status, func.count()).filter(JobApplication.user_id == current_user.id).group_by(JobApplication.status).all()
    job_application_status = {status: count for status, count in job_statuses}

    # Default job statuses
    default_statuses = {"Applied": 0, "Interview": 0, "Rejected": 0, "Hired": 0, "Pending": 0}
    job_application_status = {**default_statuses, **job_application_status}

    # Fix inconsistent status key casing (if necessary)
    job_application_status = {key.capitalize(): value for key, value in job_application_status.items()}

    # Skill Matching & Job Recommendations
    job_matches = []

    if latest_resume:
        resume_skills = set(filter(None, map(str.strip, latest_resume.skills.split(",")))) if latest_resume.skills else set()
        jobs = db.query(Job).all()

        for job in jobs:
            skills_required = set(job.skills_required) if isinstance(job.skills_required, list) else set()

            matched_skills = resume_skills.intersection(skills_required)

            if matched_skills:
                match_score = int((len(matched_skills) / len(skills_required)) * 100) if skills_required else 100
                existing_match = db.query(JobMatch).filter_by(user_id=current_user.id, resume_id=latest_resume.id, job_id=job.id).first()

                if not existing_match:
                    new_match = JobMatch(
                        user_id=current_user.id,
                        resume_id=latest_resume.id,
                        job_id=job.id,
                        match_score=match_score
                    )
                    db.add(new_match)

                job_matches.append({"job_id": job.id, "match_score": match_score})

    db.commit()

    # Update or create dashboard entry
    if not dashboard:
        dashboard = Dashboard(
            user_id=current_user.id,
            total_resumes=total_resumes,
            latest_resume_id=latest_resume.id if latest_resume else None,
            best_resume_id=best_resume.id if best_resume else None,
            resume_score=latest_resume.score if latest_resume else 0,
            average_resume_score=db.query(func.avg(Resume.score)).filter(Resume.user_id == current_user.id).scalar() or 0,
            total_jobs_applied=total_jobs_applied,
            job_application_status=job_application_status,
            job_matches=job_matches,
            total_job_matches=len(job_matches),
            last_updated=datetime.utcnow()
        )
        db.add(dashboard)
    else:
        dashboard.total_resumes = total_resumes
        dashboard.latest_resume_id = latest_resume.id if latest_resume else None
        dashboard.best_resume_id = best_resume.id if best_resume else None
        dashboard.resume_score = latest_resume.score if latest_resume else 0
        dashboard.average_resume_score = db.query(func.avg(Resume.score)).filter(Resume.user_id == current_user.id).scalar() or 0
        dashboard.total_jobs_applied = total_jobs_applied
        dashboard.job_application_status = job_application_status
        dashboard.job_matches = job_matches
        dashboard.total_job_matches = len(job_matches)
        dashboard.last_updated = datetime.utcnow()

    db.commit()

    return {"message": "Dashboard updated successfully"}
