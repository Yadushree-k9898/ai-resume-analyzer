from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from app.core.database import get_db
from app.models.resume import Resume
from app.models.user import User
from app.api.routes.scoring import calculate_resume_score
from app.api.routes.jobs import get_jobs
from app.api.routes.skills import analyze_skills
from app.api.routes.auth import get_current_user
import logging
from typing import Dict, Any, List

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/dashboard")
async def get_dashboard(
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db)
) -> Dict[str, Any]:
    """
    Fetches the user's dashboard with resume scores, job matches, and skill gaps.
    """

    if not current_user:
        logger.error("Authentication failed: No user found")
        raise HTTPException(status_code=401, detail="User authentication failed")

    user_id = current_user.id
    logger.info(f"Fetching dashboard for User ID: {user_id}")

    # Fetch resumes
    resumes = (
        db.query(Resume)
        .filter(Resume.user_id == user_id)
        .options(joinedload(Resume.user))
        .all()
    )

    if not resumes:
        logger.warning(f"No resumes found for User ID {user_id}")
        return {
            "dashboard": [],
            "total_resumes": 0,
            "message": "No resumes found. Upload a resume to get insights."
        }

    dashboard_data = []

    for resume in resumes:
        try:
            logger.info(f"Processing Resume ID: {resume.id}")

            # Ensure extracted_text exists and is a valid string
            if not resume.extracted_text or not isinstance(resume.extracted_text, str):
                logger.warning(f"Skipping Resume ID {resume.id}: Missing or invalid extracted_text")
                continue  

            extracted_text = resume.extracted_text.strip()
            logger.debug(f"Extracted Text (first 100 chars): {extracted_text[:100]}")

            # ✅ Fetch Resume Score (Ensure required job_requirements parameter is passed)
            job_requirements = {"skills": [], "experience": 0}  # Default values
            score_data = calculate_resume_score({"skills": [], "experience": 0}, job_requirements)

            if isinstance(score_data, dict):  
                score = score_data.get("overall_score", 0)
                suggestions = score_data.get("missing_skills", [])
            else:
                score, suggestions = 0, ["Error calculating score"]

            if not isinstance(suggestions, list):
                suggestions = [suggestions] if suggestions else ["No suggestions available"]

            # ✅ Fetch Job Matches with Error Handling
            try:
                job_matches = get_jobs(extracted_text) or ["No suitable jobs found"]
            except Exception as e:
                logger.error(f"Error fetching job matches for Resume ID {resume.id}: {e}")
                job_matches = ["Error fetching job matches"]

            # ✅ Analyze Skills with Error Handling
            try:
                skills_analysis = await analyze_skills(extracted_text)  # ✅ Await properly
                resume_skills = skills_analysis.get("resume_skills", [])
                missing_skills = skills_analysis.get("missing_skills", [])
            except Exception as e:
                logger.error(f"Error analyzing skills for Resume ID {resume.id}: {e}")
                resume_skills, missing_skills = [], ["Error analyzing skills"]

            # ✅ Resume Summary (Limit to 500 characters)
            resume_summary = extracted_text[:500] + "..." if len(extracted_text) > 500 else extracted_text

            dashboard_data.append({
                "resume_id": resume.id,
                "uploaded_at": resume.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "score": score,
                "suggestions": suggestions,
                "job_matches": job_matches,
                "resume_skills": resume_skills,
                "missing_skills": missing_skills,
                "resume_summary": resume_summary
            })

        except Exception as e:
            logger.error(f"Error processing Resume ID {resume.id}: {e}", exc_info=True)
            continue  # Skip this resume instead of failing the entire response

    return {
        "dashboard": dashboard_data,
        "total_resumes": len(dashboard_data)
    }
