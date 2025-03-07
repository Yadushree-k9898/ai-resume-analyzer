import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, resume, scoring, jobs
from app.core.database import Base, engine

# ✅ Load environment variables
load_dotenv()

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully!")
    except Exception as e:
        print(f"❌ Error creating tables: {e}")

@app.on_event("startup")
def startup_event():
    print("🚀 Starting AI Resume Analyzer Backend...")
    create_tables()
    try:
        with engine.connect():
            print("✅ Database connected successfully!")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(resume.router, prefix="/resumes", tags=["Resumes"])
app.include_router(scoring.router, prefix="/scoring", tags=["Scoring"])
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])

@app.get("/")
def root():
    return {"message": "🚀 AI Resume Analyzer is running!"}
