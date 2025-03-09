from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
import requests
import spacy
import os
import base64
from typing import List
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from app.models.job import Job
from app.core.database import get_db

# Load environment variables
load_dotenv()

router = APIRouter()

# Get API credentials from .env
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
JSEARCH_API = os.getenv("JSEARCH_API")

if not RAPIDAPI_KEY or not JSEARCH_API:
    raise ValueError("🚨 Missing API credentials! Make sure RAPIDAPI_KEY and JSEARCH_API are set in your .env file.")

HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com",
}

# Load NLP model for skill extraction
nlp = spacy.load("en_core_web_sm")

def extract_skills(text: str) -> List[str]:
    """Extracts skills from text using NLP."""
    doc = nlp(text)
    skills = {token.text.lower() for token in doc if token.pos_ == "NOUN" and not token.is_stop}
    return list(skills)

def decode_job_id(encoded_id: str) -> str:
    """Decodes a Base64 encoded job ID, if applicable."""
    try:
        decoded_bytes = base64.b64decode(encoded_id)
        return decoded_bytes.decode("utf-8")
    except Exception:
        return encoded_id  # Return original if decoding fails

def fetch_jobs_from_api(params: dict):
    """Helper function to fetch jobs from JSearch API with proper error handling."""
    if not JSEARCH_API.startswith("http"):
        raise HTTPException(status_code=500, detail="❌ Invalid API URL in environment variables.")
    try:
        response = requests.get(JSEARCH_API, headers=HEADERS, params=params)
        if response.status_code == 401:
            raise HTTPException(status_code=401, detail="🚨 Unauthorized: Check API Key.")
        elif response.status_code == 403:
            raise HTTPException(status_code=403, detail="🚨 Forbidden: Subscription issue with API.")
        elif response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=f"❌ API Error: {response.text}")
        data = response.json()
        jobs = data.get("data", [])
        # Decode job IDs and store as "decoded_job_id"
        for job in jobs:
            if "job_id" in job:
                job["decoded_job_id"] = decode_job_id(job["job_id"])
        return {"success": True, "jobs": jobs}
    except requests.RequestException as e:
        print(f"API Request failed: {e}")
        raise HTTPException(status_code=500, detail="❌ API Request failed. Check server logs.")
    except ValueError:
        raise HTTPException(status_code=500, detail="❌ Invalid JSON response from API.")

@router.get("/jobs")
def get_jobs(query: str, location: str = "", num_pages: int = 1, db: Session = Depends(get_db)):
    """
    Fetch job listings from the JSearch API and store new listings in the database.
    """
    params = {"query": query, "location": location, "num_pages": num_pages}
    job_data = fetch_jobs_from_api(params)
    if not job_data["success"]:
        raise HTTPException(status_code=500, detail="Failed to fetch jobs from API")
    
    jobs = job_data["jobs"]
    stored_jobs = []
    
    for job in jobs:
        # Use the decoded job ID if available; otherwise, use the original job_id.
        external_job_id = job.get("decoded_job_id") or job.get("job_id")
        # Check if a job with this external_id already exists.
        existing_job = db.query(Job).filter(Job.external_id == external_job_id).first()
        if not existing_job:
            # First, try to get skills from the API. If not present, extract from job title.
            skills = job.get("skills_required")
            if not skills:
                # Use job_title as a fallback for skill extraction.
                skills = extract_skills(job.get("job_title", ""))
            new_job = Job(
                external_id=external_job_id,  # Store the external job ID here.
                title=job.get("job_title", "Unknown Job"),
                description=job.get("job_description", "No description provided"),
                skills_required=skills,
                company_name=job.get("employer_name", "Unknown Company"),
                # Use "job_location" if provided; otherwise default.
                location=job.get("job_location", "Not specified"),
                job_type=job.get("job_employment_type", "Unknown"),
            )
            db.add(new_job)
            stored_jobs.append(new_job)
    
    db.commit()
    return {"message": "✅ Jobs stored successfully!", "stored_jobs": len(stored_jobs)}

# Request model for matching jobs based on resume text
class ResumeTextRequest(BaseModel):
    resume_text: str
    location: str = ""
    num_pages: int = 1

@router.post("/match_jobs/")
def match_jobs(request: ResumeTextRequest):
    """
    Matches jobs based on extracted skills from resume text.
    """
    keywords = extract_skills(request.resume_text)
    query = " ".join(keywords) if keywords else "software engineer"
    params = {"query": query, "location": request.location, "num_pages": request.num_pages}
    return fetch_jobs_from_api(params)
