

# from fastapi import APIRouter, Form
# import spacy

# router = APIRouter()
# nlp = spacy.load("en_core_web_sm")

# def extract_skills(text: str):
#     doc = nlp(text)
#     skills = {ent.text for ent in doc.ents if ent.label_ in ["SKILL", "TECHNOLOGY"]}
#     return skills

# @router.post("/skills")
# def analyze_skills(resume_text: str = Form(...), job_description: str = Form(...)):
#     resume_skills = extract_skills(resume_text)
#     job_skills = extract_skills(job_description)
#     missing_skills = job_skills - resume_skills
    
#     return {
#         "resume_skills": list(resume_skills),
#         "job_skills": list(job_skills),
#         "missing_skills": list(missing_skills),
#         "recommendations": "Consider learning these skills to match the job description."
#     }




from fastapi import APIRouter, Form, HTTPException
import spacy
from transformers import pipeline
import requests

router = APIRouter()

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load Hugging Face model for better skill extraction
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")

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
    url = "https://jsearch.p.rapidapi.com/search"
    querystring = {"query": job_title, "page": "1", "num_pages": "1"}
    headers = {
        "X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY",
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }
    
    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        if "data" in data and len(data["data"]) > 0:
            return data["data"][0]["description"]
    except Exception:
        pass

    return None

@router.post("/skills")
def analyze_skills(resume_text: str = Form(...), job_description: str = Form(None), job_title: str = Form(None)):
    """Analyzes skills from resume, compares with job description, and suggests missing skills."""
    if not resume_text:
        raise HTTPException(status_code=400, detail="Resume text is required.")

    # If job description is not provided, fetch it from an API
    if not job_description and job_title:
        job_description = fetch_job_description(job_title)
        if not job_description:
            raise HTTPException(status_code=400, detail="Could not fetch job description.")

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description) if job_description else set()

    missing_skills = job_skills - resume_skills
    
    return {
        "resume_skills": list(resume_skills),
        "job_skills": list(job_skills),
        "missing_skills": list(missing_skills),
        "recommendations": "Consider learning these skills to match the job description."
    }
