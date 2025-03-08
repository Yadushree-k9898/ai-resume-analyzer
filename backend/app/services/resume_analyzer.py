from textblob import TextBlob
import spacy
from app.services.resume_scorer import analyze_resume_quality

# Load the small English model
nlp = spacy.load("en_core_web_sm")

def analyze_resume_quality_service(text: str):
    """Analyze resume quality by calling the scoring function from the scorer service."""
    return analyze_resume_quality(text)
    
def analyze_grammar(text: str):
    """Simple grammar check using TextBlob: penalize for sentence structure issues."""
    blob = TextBlob(text)
    grammar_issues = sum(1 for sentence in blob.sentences if len(sentence.words) < 4 or sentence.sentiment.polarity < 0.2)
    # Penalize 2 points for each sentence with issues
    return min(10, grammar_issues * 2)

def analyze_resume_structure(text: str):
    """Analyze resume structure: Check for presence of critical sections like experience, skills, education."""
    doc = nlp(text)

    has_experience = any(token.text.lower() in ["experience", "work history"] for token in doc)
    has_education = any(token.text.lower() in ["education", "degree", "academic"] for token in doc)
    has_skills = any(token.text.lower() in ["skills", "technologies", "tools"] for token in doc)

    return {
        "has_experience": has_experience,
        "has_education": has_education,
        "has_skills": has_skills
    }
