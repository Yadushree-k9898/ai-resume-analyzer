import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "AI Resume Analyzer"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/resume_db")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "your_secret_key")
    JWT_ALGORITHM: str = "HS256"

settings = Settings()
