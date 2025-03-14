# # from fastapi import APIRouter, Depends, HTTPException
# # from sqlalchemy.orm import Session
# # from datetime import datetime
# # from typing import Dict, Any

# # from app.models.dashboard import Dashboard
# # from app.models.user import User
# # from app.models.resume import Resume
# # from app.models.job_application import JobApplication
# # from app.core.database import get_db
# # from app.api.routes.auth import get_current_user
# # from sqlalchemy.sql import func

# # router = APIRouter()

# # # -----------------------------------------------
# # # 📌 Get Dashboard Data
# # # -----------------------------------------------
# # @router.get("/dashboard", response_model=Dict[str, Any])
# # async def get_dashboard(
# #     current_user: User = Depends(get_current_user),
# #     db: Session = Depends(get_db)
# # ):
# #     """Fetch the user's dashboard data."""

# #     if not current_user:
# #         raise HTTPException(status_code=401, detail="Unauthorized user")

# #     # Fetch dashboard entry
# #     dashboard = db.query(Dashboard).filter(Dashboard.user_id == current_user.id).first()

# #     if not dashboard:
# #         return {
# #             "dashboard": None,
# #             "message": "No dashboard data available. Upload a resume or apply for jobs."
# #         }

# #     return {
# #         "dashboard": {
# #             "total_resumes": dashboard.total_resumes,
# #             "latest_resume_id": dashboard.latest_resume_id,
# #             "best_resume_id": dashboard.best_resume_id,
# #             "resume_score": dashboard.resume_score,
# #             "average_resume_score": dashboard.average_resume_score,
# #             "total_jobs_applied": dashboard.total_jobs_applied,
# #             "job_application_status": dashboard.job_application_status,
# #             "job_matches": dashboard.job_matches,
# #             "total_job_matches": dashboard.total_job_matches,
# #             "missing_skills": dashboard.missing_skills,
# #             "skills_analysis": dashboard.skills_analysis,
# #             "last_updated": dashboard.last_updated.strftime("%Y-%m-%d %H:%M:%S"),
# #         },
# #         "message": "Dashboard fetched successfully"
# #     }

# # # -----------------------------------------------
# # # 📌 Update Dashboard After Resume Upload or Job Application
# # # -----------------------------------------------
# # @router.put("/dashboard/update")
# # async def update_dashboard(
# #     current_user: User = Depends(get_current_user),
# #     db: Session = Depends(get_db)
# # ):
# #     """Update dashboard data when a user uploads a resume or applies for a job."""

# #     if not current_user:
# #         raise HTTPException(status_code=401, detail="Unauthorized user")

# #     # Fetch existing dashboard
# #     dashboard = db.query(Dashboard).filter(Dashboard.user_id == current_user.id).first()

# #     # Fetch user-related resume data
# #     total_resumes = db.query(Resume).filter(Resume.user_id == current_user.id).count()
# #     latest_resume = db.query(Resume).filter(Resume.user_id == current_user.id).order_by(Resume.created_at.desc()).first()
# #     best_resume = db.query(Resume).filter(Resume.user_id == current_user.id).order_by(Resume.score.desc()).first()

# #     # Fetch job application data
# #     total_jobs_applied = db.query(JobApplication).filter(JobApplication.user_id == current_user.id).count()
# #     job_statuses = db.query(JobApplication.status, func.count()).filter(JobApplication.user_id == current_user.id).group_by(JobApplication.status).all()
# #     job_application_status = {status: count for status, count in job_statuses}

# #     # Ensure default values for job application status
# #     default_statuses = {"Applied": 0, "Interview": 0, "Rejected": 0, "Hired": 0}
# #     job_application_status = {**default_statuses, **job_application_status}

# #     if not dashboard:
# #         # Create a new dashboard entry if it doesn't exist
# #         dashboard = Dashboard(
# #             user_id=current_user.id,
# #             total_resumes=total_resumes,
# #             latest_resume_id=latest_resume.id if latest_resume else None,
# #             best_resume_id=best_resume.id if best_resume else None,
# #             resume_score=latest_resume.score if latest_resume else 0,
# #             average_resume_score=db.query(func.avg(Resume.score)).filter(Resume.user_id == current_user.id).scalar() or 0,
# #             total_jobs_applied=total_jobs_applied,
# #             job_application_status=job_application_status,
# #             job_matches=[],
# #             total_job_matches=0,
# #             missing_skills=[],
# #             skills_analysis={},
# #             last_updated=datetime.utcnow()
# #         )
# #         db.add(dashboard)
# #     else:
# #         # Update existing dashboard
# #         dashboard.total_resumes = total_resumes
# #         dashboard.latest_resume_id = latest_resume.id if latest_resume else None
# #         dashboard.best_resume_id = best_resume.id if best_resume else None
# #         dashboard.resume_score = latest_resume.score if latest_resume else 0
# #         dashboard.average_resume_score = db.query(func.avg(Resume.score)).filter(Resume.user_id == current_user.id).scalar() or 0
# #         dashboard.total_jobs_applied = total_jobs_applied
# #         dashboard.job_application_status = job_application_status
# #         dashboard.last_updated = datetime.utcnow()

# #     db.commit()

# #     return {"message": "Dashboard updated successfully"}

# # # -----------------------------------------------
# # # 📌 Delete Dashboard Data (Optional)
# # # -----------------------------------------------
# # @router.delete("/dashboard")
# # async def delete_dashboard(
# #     current_user: User = Depends(get_current_user),
# #     db: Session = Depends(get_db)
# # ):
# #     """Delete the dashboard data for a user."""

# #     dashboard = db.query(Dashboard).filter(Dashboard.user_id == current_user.id).first()

# #     if not dashboard:
# #         raise HTTPException(status_code=404, detail="Dashboard not found")

# #     db.delete(dashboard)
# #     db.commit()

# #     return {"message": "Dashboard deleted successfully"}




# # from fastapi import APIRouter, Depends, HTTPException
# # from sqlalchemy.orm import Session
# # from datetime import datetime
# # from typing import Dict, Any, List

# # from app.models.dashboard import Dashboard
# # from app.models.user import User
# # from app.models.resume import Resume
# # from app.models.job_application import JobApplication
# # from app.models.job import Job  # Ensure this is imported
# # from app.core.database import get_db
# # from app.api.routes.auth import get_current_user
# # from sqlalchemy.sql import func

# # router = APIRouter()

# # # -----------------------------------------------
# # # 📌 Get Dashboard Data
# # # -----------------------------------------------
# # @router.get("/dashboard", response_model=Dict[str, Any])
# # async def get_dashboard(
# #     current_user: User = Depends(get_current_user),
# #     db: Session = Depends(get_db)
# # ):
# #     """Fetch the user's dashboard data."""

# #     dashboard = db.query(Dashboard).filter(Dashboard.user_id == current_user.id).first()

# #     if not dashboard:
# #         return {
# #             "dashboard": None,
# #             "message": "No dashboard data available. Upload a resume or apply for jobs."
# #         }

# #     return {
# #         "dashboard": {
# #             "total_resumes": dashboard.total_resumes,
# #             "latest_resume_id": dashboard.latest_resume_id,
# #             "best_resume_id": dashboard.best_resume_id,
# #             "resume_score": dashboard.resume_score,
# #             "average_resume_score": dashboard.average_resume_score,
# #             "total_jobs_applied": dashboard.total_jobs_applied,
# #             "job_application_status": dashboard.job_application_status or {},
# #             "job_matches": dashboard.job_matches or [],
# #             "total_job_matches": dashboard.total_job_matches,
# #             "missing_skills": dashboard.missing_skills or [],
# #             "skills_analysis": dashboard.skills_analysis or {},
# #             "last_updated": dashboard.last_updated.strftime("%Y-%m-%d %H:%M:%S"),
# #         },
# #         "message": "Dashboard fetched successfully"
# #     }


# # # -----------------------------------------------
# # # 📌 Update Dashboard After Resume Upload or Job Application
# # # -----------------------------------------------
# # @router.put("/dashboard/update")
# # async def update_dashboard(
# #     current_user: User = Depends(get_current_user),
# #     db: Session = Depends(get_db)
# # ):
# #     """Update dashboard data when a user uploads a resume or applies for a job."""

# #     dashboard = db.query(Dashboard).filter(Dashboard.user_id == current_user.id).first()

# #     # Fetch user-related resume data
# #     total_resumes = db.query(Resume).filter(Resume.user_id == current_user.id).count()
# #     latest_resume = db.query(Resume).filter(Resume.user_id == current_user.id).order_by(Resume.created_at.desc()).first()
# #     best_resume = db.query(Resume).filter(Resume.user_id == current_user.id).order_by(Resume.score.desc()).first()

# #     # Fetch job application data
# #     total_jobs_applied = db.query(JobApplication).filter(JobApplication.user_id == current_user.id).count()
# #     job_statuses = db.query(JobApplication.status, func.count()).filter(JobApplication.user_id == current_user.id).group_by(JobApplication.status).all()
# #     job_application_status = {status: count for status, count in job_statuses}

# #     # Default job statuses
# #     default_statuses = {"Applied": 0, "Interview": 0, "Rejected": 0, "Hired": 0, "Pending": 0}
# #     job_application_status = {**default_statuses, **job_application_status}

# #     # Skill Matching & Job Recommendations
# #     job_matches = []
# #     missing_skills = set()
# #     skills_analysis = {}

# #     if latest_resume:
# #         print(f"📌 Latest Resume ID: {latest_resume.id}")

# #         # Convert skills into a set (handle comma-separated strings)
# #         resume_skills = set(latest_resume.skills.split(",")) if latest_resume.skills else set()
# #         print(f"🔍 Resume Skills: {resume_skills}")

# #         # Fetch all jobs
# #         jobs = db.query(Job).all()
# #         print(f"📌 Found {len(jobs)} jobs in DB.")

# #         for job in jobs:
# #             required_skills = set(job.required_skills.split(",")) if job.required_skills else set()
# #             matched_skills = resume_skills.intersection(required_skills)
# #             job_missing_skills = required_skills - resume_skills

# #             if matched_skills:
# #                 job_matches.append(job.id)

# #             missing_skills.update(job_missing_skills)

# #         skills_analysis = {
# #             "total_skills": len(resume_skills),
# #             "strong_skills": list(resume_skills),
# #             "missing_skills_count": len(missing_skills),
# #             "missing_skills": list(missing_skills),
# #         }

# #         print(f"✅ Matched Jobs: {job_matches}")
# #         print(f"⚠️ Missing Skills: {missing_skills}")
# #         print(f"📊 Skills Analysis: {skills_analysis}")

# #     # Update or create dashboard entry
# #     if not dashboard:
# #         dashboard = Dashboard(
# #             user_id=current_user.id,
# #             total_resumes=total_resumes,
# #             latest_resume_id=latest_resume.id if latest_resume else None,
# #             best_resume_id=best_resume.id if best_resume else None,
# #             resume_score=latest_resume.score if latest_resume else 0,
# #             average_resume_score=db.query(func.avg(Resume.score)).filter(Resume.user_id == current_user.id).scalar() or 0,
# #             total_jobs_applied=total_jobs_applied,
# #             job_application_status=job_application_status,
# #             job_matches=job_matches,
# #             total_job_matches=len(job_matches),
# #             missing_skills=list(missing_skills),
# #             skills_analysis=skills_analysis,
# #             last_updated=datetime.utcnow()
# #         )
# #         db.add(dashboard)
# #     else:
# #         dashboard.total_resumes = total_resumes
# #         dashboard.latest_resume_id = latest_resume.id if latest_resume else None
# #         dashboard.best_resume_id = best_resume.id if best_resume else None
# #         dashboard.resume_score = latest_resume.score if latest_resume else 0
# #         dashboard.average_resume_score = db.query(func.avg(Resume.score)).filter(Resume.user_id == current_user.id).scalar() or 0
# #         dashboard.total_jobs_applied = total_jobs_applied
# #         dashboard.job_application_status = job_application_status
# #         dashboard.job_matches = job_matches
# #         dashboard.total_job_matches = len(job_matches)
# #         dashboard.missing_skills = list(missing_skills)
# #         dashboard.skills_analysis = skills_analysis
# #         dashboard.last_updated = datetime.utcnow()

# #     db.commit()

# #     return {"message": "Dashboard updated successfully"}


# # # -----------------------------------------------
# # # 📌 Delete Dashboard Data
# # # -----------------------------------------------
# # @router.delete("/dashboard")
# # async def delete_dashboard(
# #     current_user: User = Depends(get_current_user),
# #     db: Session = Depends(get_db)
# # ):
# #     """Delete the dashboard data for a user."""

# #     dashboard = db.query(Dashboard).filter(Dashboard.user_id == current_user.id).first()

# #     if not dashboard:
# #         raise HTTPException(status_code=404, detail="Dashboard not found")

# #     db.delete(dashboard)
# #     db.commit()

# #     return {"message": "Dashboard deleted successfully"}



# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from datetime import datetime
# from typing import Dict, Any, List

# from app.models.dashboard import Dashboard
# from app.models.user import User
# from app.models.resume import Resume
# from app.models.job_application import JobApplication
# from app.models.job import Job  # Ensure this is imported
# from app.core.database import get_db
# from app.api.routes.auth import get_current_user
# from sqlalchemy.sql import func

# router = APIRouter()

# # -----------------------------------------------
# # 📌 Get Dashboard Data
# # -----------------------------------------------
# @router.get("/dashboard", response_model=Dict[str, Any])
# async def get_dashboard(
#     current_user: User = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """Fetch the user's dashboard data."""

#     dashboard = db.query(Dashboard).filter(Dashboard.user_id == current_user.id).first()

#     if not dashboard:
#         return {
#             "dashboard": None,
#             "message": "No dashboard data available. Upload a resume or apply for jobs."
#         }

#     return {
#         "dashboard": {
#             "total_resumes": dashboard.total_resumes,
#             "latest_resume_id": dashboard.latest_resume_id,
#             "best_resume_id": dashboard.best_resume_id,
#             "resume_score": dashboard.resume_score,
#             "average_resume_score": dashboard.average_resume_score,
#             "total_jobs_applied": dashboard.total_jobs_applied,
#             "job_application_status": dashboard.job_application_status or {},
#             "job_matches": dashboard.job_matches or [],
#             "total_job_matches": dashboard.total_job_matches,
#             "last_updated": dashboard.last_updated.strftime("%Y-%m-%d %H:%M:%S"),
#         },
#         "message": "Dashboard fetched successfully"
#     }


# # -----------------------------------------------
# # 📌 Update Dashboard After Resume Upload or Job Application
# # -----------------------------------------------
# @router.put("/dashboard/update")
# async def update_dashboard(
#     current_user: User = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """Update dashboard data when a user uploads a resume or applies for a job."""

#     dashboard = db.query(Dashboard).filter(Dashboard.user_id == current_user.id).first()

#     # Fetch user-related resume data
#     total_resumes = db.query(Resume).filter(Resume.user_id == current_user.id).count()
#     latest_resume = db.query(Resume).filter(Resume.user_id == current_user.id).order_by(Resume.created_at.desc()).first()
#     best_resume = db.query(Resume).filter(Resume.user_id == current_user.id).order_by(Resume.score.desc()).first()

#     # Fetch job application data
#     total_jobs_applied = db.query(JobApplication).filter(JobApplication.user_id == current_user.id).count()
#     job_statuses = db.query(JobApplication.status, func.count()).filter(JobApplication.user_id == current_user.id).group_by(JobApplication.status).all()
#     job_application_status = {status: count for status, count in job_statuses}

#     # Default job statuses
#     default_statuses = {"Applied": 0, "Interview": 0, "Rejected": 0, "Hired": 0, "Pending": 0}
#     job_application_status = {**default_statuses, **job_application_status}

#     # Skill Matching & Job Recommendations
#     job_matches = []

#     if latest_resume:
#         print(f"📌 Latest Resume ID: {latest_resume.id}")

#         # Convert skills into a set (handle comma-separated strings)
#         resume_skills = set(latest_resume.skills.split(",")) if latest_resume.skills else set()
#         print(f"🔍 Resume Skills: {resume_skills}")

#         # Fetch all jobs
#         jobs = db.query(Job).all()
#         print(f"📌 Found {len(jobs)} jobs in DB.")

#         for job in jobs:
#             required_skills = set(job.required_skills.split(",")) if job.required_skills else set()
#             print(f"🎯 Job ID {job.id} - Required Skills: {required_skills}")

#             matched_skills = resume_skills.intersection(required_skills)
#             print(f"✅ Matched Skills for Job {job.id}: {matched_skills}")

#             if matched_skills:
#                 job_matches.append(job.id)

#         print(f"🚀 Final Job Matches: {job_matches}")

#     # Update or create dashboard entry
#     if not dashboard:
#         dashboard = Dashboard(
#             user_id=current_user.id,
#             total_resumes=total_resumes,
#             latest_resume_id=latest_resume.id if latest_resume else None,
#             best_resume_id=best_resume.id if best_resume else None,
#             resume_score=latest_resume.score if latest_resume else 0,
#             average_resume_score=db.query(func.avg(Resume.score)).filter(Resume.user_id == current_user.id).scalar() or 0,
#             total_jobs_applied=total_jobs_applied,
#             job_application_status=job_application_status,
#             job_matches=job_matches,
#             total_job_matches=len(job_matches),
#             last_updated=datetime.utcnow()
#         )
#         db.add(dashboard)
#     else:
#         dashboard.total_resumes = total_resumes
#         dashboard.latest_resume_id = latest_resume.id if latest_resume else None
#         dashboard.best_resume_id = best_resume.id if best_resume else None
#         dashboard.resume_score = latest_resume.score if latest_resume else 0
#         dashboard.average_resume_score = db.query(func.avg(Resume.score)).filter(Resume.user_id == current_user.id).scalar() or 0
#         dashboard.total_jobs_applied = total_jobs_applied
#         dashboard.job_application_status = job_application_status
#         dashboard.job_matches = job_matches
#         dashboard.total_job_matches = len(job_matches)
#         dashboard.last_updated = datetime.utcnow()

#     db.commit()

#     return {"message": "Dashboard updated successfully"}


# # -----------------------------------------------
# # 📌 Delete Dashboard Data
# # -----------------------------------------------
# @router.delete("/dashboard")
# async def delete_dashboard(
#     current_user: User = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     """Delete the dashboard data for a user."""

#     dashboard = db.query(Dashboard).filter(Dashboard.user_id == current_user.id).first()

#     if not dashboard:
#         raise HTTPException(status_code=404, detail="Dashboard not found")

#     db.delete(dashboard)
#     db.commit()

#     return {"message": "Dashboard deleted successfully"}


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

    job_matches = [
        {"job_id": match.job_id, "match_score": match.match_score}
        for match in db.query(JobMatch).filter_by(user_id=current_user.id).all()
    ]

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

    # Skill Matching & Job Recommendations
    job_matches = []

    if latest_resume:
        resume_skills = set(filter(None, map(str.strip, latest_resume.skills.split(",")))) if latest_resume.skills else set()
        jobs = db.query(Job).all()

        for job in jobs:
            required_skills = set(filter(None, map(str.strip, job.required_skills.split(",")))) if job.required_skills else set()
            matched_skills = resume_skills.intersection(required_skills)

            if matched_skills:
                match_score = int((len(matched_skills) / len(required_skills)) * 100) if required_skills else 100
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

# -----------------------------------------------
# 📌 Delete Dashboard Data
# -----------------------------------------------
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
