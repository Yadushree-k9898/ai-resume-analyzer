from fastapi import APIRouter
import spacy

router = APIRouter()
nlp = spacy.load("en_core_web_sm")

def score_resume(text):
    doc = nlp(text)
    word_count = len(doc)
    score = min(100, word_count // 5)  # Simple scoring based on word count
    return score

@router.post("/score")
def analyze_resume(resume_text: str):
    score = score_resume(resume_text)
    return {"resume_score": score, "suggestions": "Use more action verbs, quantify achievements"}
