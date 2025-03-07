from fuzzywuzzy import fuzz
from .resume_analyzer import analyze_resume_quality

def match_job_with_resume(resume_text: str, job_description: str):
    """Match resume skills with job requirements and calculate a match percentage."""
    resume_analysis = analyze_resume_quality(resume_text)
    match_score = fuzz.token_set_ratio(resume_text, job_description)

    recommendations = (
        "Consider improving your resume with better keywords."
        if match_score < 50
        else "You are a strong match!"
    )

    return {"match_score": match_score, "recommendations": recommendations}
