from fastapi import APIRouter, Form
from textblob import TextBlob
import spacy
from app.services.resume_analyzer import analyze_resume_quality


router = APIRouter()

@router.post("/analyze")
async def get_resume_score(resume_text: str = Form(...)):
    """Analyze resume text and return a score."""
    return analyze_resume_quality(resume_text)
