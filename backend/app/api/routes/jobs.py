from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests
import spacy
import os
from typing import List
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

router = APIRouter()

# ✅ Get API key from .env
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
JSEARCH_API = "https://jsearch.p.rapidapi.com/search"

if not RAPIDAPI_KEY:
    raise ValueError("🚨 RAPIDAPI_KEY is missing! Check your .env file.")

HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com",
}

# Load NLP model for skill extraction
nlp = spacy.load("en_core_web_sm")

def extract_skills(text: str) -> List[str]:
    """Extracts skills from resume text using NLP."""
    doc = nlp(text)
    return list(set([token.text.lower() for token in doc if token.pos_ == "NOUN"]))

@router.get("/")
def get_jobs(query: str, location: str = "", num_pages: int = 1):
    """Fetch job listings from RapidAPI's JSearch API."""
    params = {"query": query, "location": location, "num_pages": num_pages}
    
    response = requests.get(JSEARCH_API, headers=HEADERS, params=params)

    if response.status_code == 401:
        raise HTTPException(status_code=401, detail="🚨 Unauthorized: Check API Key.")
    elif response.status_code == 403:
        raise HTTPException(status_code=403, detail="🚨 Forbidden: You are not subscribed to this API.")
    elif response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=f"❌ API Error: {response.text}")

    try:
        data = response.json()
        return {"jobs": data.get("data", [])}
    except ValueError:
        raise HTTPException(status_code=500, detail="Invalid JSON response from API.")

# ✅ Request model for /match_jobs
class ResumeTextRequest(BaseModel):
    resume_text: str
    location: str = ""
    num_pages: int = 1

@router.post("/match_jobs/")
def match_jobs(request: ResumeTextRequest):
    """Matches jobs based on extracted keywords from resume."""
    keywords = extract_skills(request.resume_text)
    query = " ".join(keywords) if keywords else "software engineer"

    params = {"query": query, "location": request.location, "num_pages": request.num_pages}
    response = requests.get(JSEARCH_API, headers=HEADERS, params=params)

    if response.status_code == 401:
        raise HTTPException(status_code=401, detail="🚨 Unauthorized: Check API Key.")
    elif response.status_code == 403:
        raise HTTPException(status_code=403, detail="🚨 Forbidden: You are not subscribed to this API.")
    elif response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=f"❌ API Error: {response.text}")

    try:
        data = response.json()
        return {"matched_jobs": data.get("data", [])}
    except ValueError:
        raise HTTPException(status_code=500, detail="Invalid JSON response from API.")
