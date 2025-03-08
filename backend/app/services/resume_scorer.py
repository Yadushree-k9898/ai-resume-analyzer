from textblob import TextBlob
import spacy
import re

# Load the small English model
nlp = spacy.load("en_core_web_sm")

def analyze_resume_quality(text: str):
    """Analyze resume quality based on structure, clarity, keyword density, and ATS-like requirements."""
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

    # Score calculation
    score = 0
    # Check presence of key sections and assign points
    score += 20 if has_experience else 0
    score += 20 if has_education else 0
    score += 15 if has_skills else 0
    score += 10 if has_certifications else 0
    score += 10 if has_contact_info else 0
    score += 10 if has_objective else 0
    score += 5 if has_summary else 0

    # Add readability score: Positive readability contributes to score
    score += int(readability * 10)  # Convert polarity to score (max 10 points)

    # Keyword density - Assign points for each keyword found in the resume
    score += min(10, keyword_density * 2)  # Penalize if no keywords are found

    # If missing any section, subtract points
    if not has_experience:
        score -= 15
    if not has_education:
        score -= 15
    if not has_skills:
        score -= 10
    if not has_certifications:
        score -= 5
    if not has_contact_info:
        score -= 5
    if not has_objective:
        score -= 5
    if not has_summary:
        score -= 5

    # Score penalty for grammar issues (using textblob)
    grammar_score = analyze_grammar(text)
    score -= grammar_score  # Subtract grammar issues score (0-10)

    # ATS-friendly formatting: Check for excessive use of non-standard fonts, symbols, etc.
    ats_score = check_ats_friendly(text)
    score += ats_score  # Penalty or bonus based on ATS-friendly formatting

    # Ensure the score doesn't exceed 100 or fall below 0
    score = max(0, min(score, 100))

    # Define suggestions based on the score
    suggestions = []
    if score < 50:
        suggestions.append("Resume is missing key sections or has many issues. Consider major improvements.")
        suggestions.append("Ensure your resume includes all essential sections: Experience, Education, Skills, and Contact Info.")
        suggestions.append("Focus on making your content concise and easy to read. Avoid passive voice and overly complex sentences.")
        suggestions.append("Grammar, sentence structure, and readability need significant improvements.")
    elif score < 70:
        suggestions.append("Resume lacks important sections or has grammar issues. Consider revising your work experience and education sections.")
        suggestions.append("Improve keyword usage to match job descriptions. Focus on including specific job-related skills.")
        suggestions.append("Make sure your resume is formatted correctly and doesn't include any non-ATS-friendly elements.")
    elif score < 90:
        suggestions.append("Resume is decent but could be optimized further. Ensure proper grammar, structure, and job-specific keywords.")
        suggestions.append("Make sure your resume is ATS-friendly and easy to scan, with no unnecessary formatting elements.")
        suggestions.append("Consider adding a summary or objective statement to highlight your career goals.")
    else:
        suggestions.append("Resume is well-optimized and ATS-friendly!")
        suggestions.append("Great job! Keep the content concise, keyword-optimized, and well-structured.")
        suggestions.append("Focus on maintaining the balance between a well-written resume and ATS compatibility.")

    if grammar_score > 0:
        suggestions.append("Consider improving grammar and sentence structure. Avoid excessive use of passive voice and wordiness.")
    
    if ats_score < 0:
        suggestions.append("Avoid using excessive symbols, graphics, or non-standard fonts that could confuse an ATS system.")

    return {"resume_score": score, "suggestions": suggestions}

def analyze_grammar(text: str):
    """Simple grammar check using TextBlob: penalize for sentence structure issues."""
    blob = TextBlob(text)
    grammar_issues = sum(1 for sentence in blob.sentences if len(sentence.words) < 4 or sentence.sentiment.polarity < 0.2)
    # Penalize 2 points for each sentence with issues
    return min(10, grammar_issues * 2)

def check_ats_friendly(text: str):
    """Check if resume is ATS-friendly (e.g., no excessive symbols, headers, or graphics)."""
    # ATS may have issues with special characters, fonts, or formatting
    special_characters = re.findall(r'[^a-zA-Z0-9\s,.\-]', text)
    
    if len(special_characters) > 5:  # Arbitrary threshold for special characters
        return -10  # Significant penalty for bad formatting

    # Check for any non-standard sections like headers, non-ATS-friendly fonts
    if any(word in text.lower() for word in ["graphics", "image", "logo"]):
        return -10  # Penalty for non-ATS-friendly elements

    return 5  # Small bonus for ATS-friendly formatting

