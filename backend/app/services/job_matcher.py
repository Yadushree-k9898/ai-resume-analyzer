import json

job_database = [
    {"title": "Software Engineer", "skills": ["Python", "Django", "SQL", "JavaScript"]},
    {"title": "Frontend Developer", "skills": ["React.js", "JavaScript", "CSS", "HTML"]},
    {"title": "Data Analyst", "skills": ["SQL", "Python", "Pandas", "Excel"]}
]

def match_jobs(resume_skills):
    """Matches jobs based on extracted skills."""
    matched_jobs = []

    if not resume_skills:
        return matched_jobs  # No skills, no jobs matched

    for job in job_database:
        matched_skills = set(resume_skills) & set(job["skills"])
        missing_skills = list(set(job["skills"]) - matched_skills)

        if matched_skills:  # Only add jobs with at least 1 matched skill
            matched_jobs.append({
                "title": job["title"],
                "matched_skills": list(matched_skills),
                "missing_skills": missing_skills
            })

    return matched_jobs

