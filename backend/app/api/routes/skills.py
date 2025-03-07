import os
import re
import requests
from dotenv import load_dotenv
from fastapi import APIRouter, Form, HTTPException
import spacy
from transformers import pipeline

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI Router
router = APIRouter()

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load Hugging Face model for better skill extraction
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")

# Load API key from environment variable
API_KEY = os.getenv("RAPIDAPI_KEY")

# JSearch API URL and headers
url = "https://jsearch.p.rapidapi.com/search"
headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

def clean_text(text: str):
    """Cleans the extracted resume text by handling common OCR errors."""
    
    # Step 1: Fix known OCR errors and specific issues
    cleaned_text = text.replace('Y K', 'Yadushree K')  # Fix specific OCR errors
    cleaned_text = cleaned_text.replace('T K', 'Technology Skills')
    cleaned_text = cleaned_text.replace('47@', '')  # Fix unwanted characters like '47@'
    cleaned_text = cleaned_text.replace('9898 S', '')  # Remove random misplaced text like '9898 S'
    
    # Step 2: Remove excessive spaces and line breaks
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    
    # Step 3: Fix issues with random spaces between words (replace them with a single space)
    cleaned_text = re.sub(r'(\w)\s+(\w)', r'\1 \2', cleaned_text)  # Fix words with excessive space

    # Step 4: Remove numbers that are not part of valid content
    cleaned_text = re.sub(r'\d+', '', cleaned_text)  # Remove unwanted numbers

    # Step 5: Remove any remaining special characters, keeping basic punctuation
    cleaned_text = re.sub(r'[^\w\s,.-]', '', cleaned_text)
    
    # Step 6: Remove other garbage characters or fragments
    cleaned_text = re.sub(r'[^\x00-\x7F]+', '', cleaned_text)  # Remove non-ASCII characters

    # Step 7: Trim leading/trailing spaces
    cleaned_text = cleaned_text.strip()

    return cleaned_text

def extract_skills(text: str):
    """Extracts skills from text using both spaCy and Hugging Face NER."""
    doc = nlp(text)
    skills = {ent.text for ent in doc.ents if ent.label_ in ["SKILL", "TECHNOLOGY"]}

    # Extract using Hugging Face model
    entities = ner_pipeline(text)
    for entity in entities:
        if entity['entity_group'] == 'MISC':  # MISC often contains skills in resumes
            skills.add(entity['word'])

    return skills

def fetch_job_description(job_title: str):
    """Fetches job description from a job API (JSearch API)."""
    querystring = {"query": job_title, "page": "1", "num_pages": "1"}

    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        if "data" in data and len(data["data"]) > 0:
            return data["data"][0]["description"]
    except Exception as e:
        print(f"Error fetching job description: {e}")
    
    return None

@router.post("/skills")
def analyze_skills(resume_text: str = Form(...), job_description: str = Form(None), job_title: str = Form(None)):
    """Analyzes skills from resume, compares with job description, and suggests missing skills."""
    
    if not resume_text:
        raise HTTPException(status_code=400, detail="Resume text is required.")

    # Clean the resume text
    cleaned_resume_text = clean_text(resume_text)

    # If job description is not provided, fetch it from an API
    if not job_description and job_title:
        job_description = fetch_job_description(job_title)
        if not job_description:
            raise HTTPException(status_code=400, detail="Could not fetch job description.")

    # Extract skills from both cleaned resume text and job description
    resume_skills = extract_skills(cleaned_resume_text)
    job_skills = extract_skills(job_description) if job_description else set()

    # Find missing skills
    missing_skills = job_skills - resume_skills

    return {
        "resume_skills": list(resume_skills),
        "job_skills": list(job_skills),
        "missing_skills": list(missing_skills),
        "recommendations": "Consider learning these skills to match the job description."
    }
