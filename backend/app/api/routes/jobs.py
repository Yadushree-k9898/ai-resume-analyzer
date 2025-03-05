from fastapi import APIRouter
import requests

router = APIRouter()

JSEARCH_API = "https://jsearch.p.rapidapi.com/search"

@router.get("/jobs")
def get_jobs(query: str):
    headers = {"X-RapidAPI-Key": "YOUR_API_KEY"}
    params = {"query": query, "num_pages": 1}
    response = requests.get(JSEARCH_API, headers=headers, params=params)
    
    if response.status_code != 200:
        return {"error": "Failed to fetch job listings"}
    
    jobs = response.json().get("data", [])
    return {"jobs": jobs}
