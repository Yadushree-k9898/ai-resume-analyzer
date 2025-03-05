from fastapi import APIRouter
import spacy

router = APIRouter()
nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    doc = nlp(text)
    skills = [ent.text for ent in doc.ents if ent.label_ in ["SKILL", "TECHNOLOGY"]]
    return set(skills)

@router.post("/skills")
def analyze_skills(resume_text: str, job_description: str):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)
    missing_skills = job_skills - resume_skills
    return {"missing_skills": list(missing_skills), "recommendations": "Consider learning these skills"}
