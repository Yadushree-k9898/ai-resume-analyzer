from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
import requests
import spacy
import os
from typing import List
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from app.models.job import Job
from app.core.database import get_db

# Load environment variables
load_dotenv()

router = APIRouter()

# Get API URL from .env
JOB_URL = os.getenv("JOB_URL")
if not JOB_URL:
    raise ValueError("🚨 Missing JOB_URL in the environment. Make sure JOB_URL is set in your .env file.")

# Load NLP model for skill extraction
nlp = spacy.load("en_core_web_sm")

def extract_skills(text: str) -> List[str]:
    """Extracts skills from text using NLP."""
    doc = nlp(text)
    skills = {token.text.lower() for token in doc if token.pos_ == "NOUN" and not token.is_stop}
    return list(skills)

def fetch_jobs_from_api(params: dict):
    """Fetch jobs from the job API with error handling."""
    print(f"\U0001F4BC Fetching jobs from {JOB_URL} with params: {params}")  # Debugging
    if not JOB_URL.startswith("http"):
        raise HTTPException(status_code=500, detail="❌ Invalid API URL in environment variables.")
    try:
        response = requests.get(JOB_URL, params=params)
        print("\U0001F50D Raw API Response:", response.text)  # Debugging
        response.raise_for_status()
        data = response.json()
        print("\U0001F4E6 Parsed API Response:", data)  # Debugging
        # The API returns jobs under the "data" key
        return {"success": True, "jobs": data.get("data", [])}
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"❌ API Request failed: {e}")

@router.get("/jobs")
def get_jobs(query: str, location: str = "", num_pages: int = 1, db: Session = Depends(get_db)):
    """
    Fetch job listings from the job API and store new listings in the database.
    """
    params = {"query": query, "location": location, "page": num_pages}
    job_data = fetch_jobs_from_api(params)
    
    if not job_data["success"]:
        raise HTTPException(status_code=500, detail="Failed to fetch jobs from API")
    
    jobs = job_data["jobs"]
    stored_jobs = []
    
    for job in jobs:
        # Use "slug" as the external job ID
        external_job_id = job.get("slug")
        if not external_job_id:
            continue  # Skip if no unique identifier
        
        # Check if a job with this external_id already exists.
        existing_job = db.query(Job).filter(Job.external_id == external_job_id).first()
        if not existing_job:
            # Try to get skills from the API; if not present, extract from job title.
            skills = job.get("skills_required")
            if not skills:
                skills = extract_skills(job.get("title", ""))
            
            # Fetch apply link from the API response (using "url" here)
            apply_link = job.get("url") or job.get("apply_link") or job.get("job_apply_link")
            if not apply_link:
                print(f"Warning: No apply link found for job {external_job_id}")  # Debugging
                apply_link = "https://example.com"  # Fallback
            
            new_job = Job(
                external_id=external_job_id,
                title=job.get("title", "Unknown Job"),
                description=job.get("description", "No description provided"),
                skills_required=skills,
                company_name=job.get("company_name", "Unknown Company"),
                location=job.get("location", "Not specified"),
                # If job_types is a list, join them; otherwise, use job_employment_type or a default value.
                job_type=", ".join(job.get("job_types", [])) if isinstance(job.get("job_types"), list) else job.get("job_employment_type", "Unknown"),
                apply_link=apply_link,
            )
            db.add(new_job)
            stored_jobs.append(new_job)
    
    db.commit()
    return {"message": "✅ Jobs stored successfully!", "stored_jobs": len(stored_jobs)}

class ResumeTextRequest(BaseModel):
    resume_text: str
    location: str = ""
    num_pages: int = 1

@router.post("/match_jobs/")
def match_jobs(request: ResumeTextRequest, db: Session = Depends(get_db)):
    """
    Matches jobs based on extracted skills from resume text.
    """
    keywords = extract_skills(request.resume_text)
    if not keywords:
        return {"message": "⚠️ No skills found in resume.", "matched_jobs": []}
    query = " ".join(keywords)
    params = {"query": query, "location": request.location, "page": request.num_pages}
    # Alternatively, you might choose to match against stored jobs in your DB.
    return fetch_jobs_from_api(params)
