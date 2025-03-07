from fastapi import APIRouter, Form
from textblob import TextBlob
import spacy

router = APIRouter()

nlp = spacy.load("en_core_web_sm")

def analyze_resume_quality(text: str):
    """Analyze resume quality based on structure, clarity, and readability."""
    doc = nlp(text)

    # Check for key resume sections
    has_experience = any(token.text.lower() in ["experience", "work history"] for token in doc)
    has_education = any(token.text.lower() in ["education", "degree"] for token in doc)
    has_skills = any(token.text.lower() in ["skills", "technologies"] for token in doc)

    # Readability score using TextBlob
    readability = TextBlob(text).sentiment.polarity  # Polarity ranges from -1 to 1

    score = 0
    score += 30 if has_experience else 0
    score += 30 if has_education else 0
    score += 20 if has_skills else 0
    score += int(readability * 20)  

    return {
        "resume_score": score,
        "suggestions": "Add missing sections to improve." if score < 80 else "Resume looks good!"
    }

@router.post("/analyze")
async def get_resume_score(resume_text: str = Form(...)):
    """Analyze resume text and return a score."""
    return analyze_resume_quality(resume_text)
