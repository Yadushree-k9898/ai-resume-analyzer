from fastapi import APIRouter, UploadFile, File
from app.services.resume_analyzer import analyze_resume_quality

router = APIRouter()

@router.post("/analyze")
async def get_resume_score(file: UploadFile = File(...)):
    """Analyze resume text from uploaded file and return a score."""
    content = await file.read()  # Read the uploaded file
    resume_text = content.decode("utf-8")  # Convert bytes to text
    return analyze_resume_quality(resume_text)  # Process and return analysis
