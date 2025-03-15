from textblob import TextBlob
import spacy
import re

# Load the small English model
nlp = spacy.load("en_core_web_sm")

def analyze_resume_quality(text: str):
    """Analyze resume quality with a more lenient scoring system."""
    doc = nlp(text)

    # Check for key resume sections
    has_experience = any(token.text.lower() in ["experience", "work history", "professional experience", "employment"] for token in doc)
    has_education = any(token.text.lower() in ["education", "degree", "academic", "university", "school", "diploma"] for token in doc)
    has_skills = any(token.text.lower() in ["skills", "technologies", "tools", "competencies", "expertise"] for token in doc)
    has_certifications = any(token.text.lower() in ["certifications", "certificates", "training", "courses"] for token in doc)
    has_contact_info = any(token.text.lower() in ["contact", "phone", "email", "address", "linkedin"] for token in doc)
    has_objective = any(token.text.lower() in ["objective", "career goal", "career summary"] for token in doc)
    has_summary = any(token.text.lower() in ["summary", "professional summary", "profile"] for token in doc)

    # Readability score using TextBlob
    readability = TextBlob(text).sentiment.polarity  # Polarity ranges from -1 to 1

    # Keyword density for job-specific keywords
    job_keywords = ["python", "javascript", "react", "machine learning", "data analysis", "project management", "developer", "java", "sql", "css", "html", "agile", "scrum", "devops"]
    keyword_density = sum(text.lower().count(keyword) for keyword in job_keywords)

    # Score calculation (Lenient Approach)
    score = 0
    score += 25 if has_experience else 0  # Increased points for experience
    score += 20 if has_education else 0
    score += 15 if has_skills else 0
    score += 10 if has_certifications else 0
    score += 10 if has_contact_info else 0
    score += 10 if has_objective else 0
    score += 5 if has_summary else 0

    # Add readability score
    score += int(readability * 10)

    # Increase keyword impact
    score += min(15, keyword_density * 3)

    # Reduced Penalties for Missing Sections
    if not has_experience:
        score -= 10
    if not has_education:
        score -= 10
    if not has_skills:
        score -= 5
    if not has_certifications:
        score -= 3
    if not has_contact_info:
        score -= 3
    if not has_objective:
        score -= 3
    if not has_summary:
        score -= 3

    # Less Strict Grammar Penalty
    grammar_score = analyze_grammar(text)
    score -= min(5, grammar_score)  # Max penalty reduced to 5

    # ATS Friendliness Adjustments
    ats_score = check_ats_friendly(text)
    score += ats_score  # Still consider formatting issues, but less harshly

    # Ensure the score remains within 0-100
    score = max(0, min(score, 100))

    # Define more lenient suggestions
    suggestions = []
    if score < 60:
        suggestions.append("Resume could be improved. Ensure key sections like Work Experience and Skills are well-detailed.")
        suggestions.append("Enhance keyword usage to better match job descriptions.")
        suggestions.append("Ensure correct formatting and ATS-friendly structure.")
    elif score < 80:
        suggestions.append("Resume is fairly strong but could benefit from slight improvements in clarity, keywords, and formatting.")
        suggestions.append("Make sure your grammar and sentence structure are clear.")
    else:
        suggestions.append("Your resume is well-structured and optimized! Keep refining it for even better results.")

    if grammar_score > 0:
        suggestions.append("Consider minor grammar refinements for better readability.")
    
    if ats_score < 0:
        suggestions.append("Avoid excessive symbols or graphics that could impact ATS scanning.")

    return {"resume_score": score, "suggestions": suggestions}


def analyze_grammar(text: str):
    """Less strict grammar check using TextBlob."""
    blob = TextBlob(text)
    grammar_issues = sum(1 for sentence in blob.sentences if len(sentence.words) < 4 or sentence.sentiment.polarity < 0.1)
    return min(5, grammar_issues)  # Max penalty reduced to 5


def check_ats_friendly(text: str):
    """Lenient ATS-friendly check."""
    special_characters = re.findall(r'[^a-zA-Z0-9\s,.-]', text)
    
    if len(special_characters) > 8:
        return -5  # Reduced penalty
    
    if any(word in text.lower() for word in ["graphics", "image", "logo"]):
        return -5  # Less strict ATS penalty
    
    return 5  # Small bonus for ATS-friendly formatting
