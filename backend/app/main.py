import os
import logging
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, resume, scoring, jobs, job_application, dashboard  
from app.core.database import Base, engine

# ✅ Load environment variables
load_dotenv()

# ✅ Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ Initialize FastAPI app
app = FastAPI(
    title="AI Resume Analyzer API",
    description="An API for analyzing resumes and matching jobs using AI.",
    version="1.0.0",
    debug=True
)

# ✅ Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def create_tables():
    """Creates database tables if they do not exist."""
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("✅ Database tables created successfully!")
    except Exception as e:
        logger.error(f"❌ Error creating tables: {e}")

@app.on_event("startup")
def startup_event():
    """Startup tasks - initializing database connection & tables."""
    logger.info("🚀 Starting AI Resume Analyzer Backend...")

    # ✅ Create tables if not exists
    create_tables()

    # ✅ Check database connection
    try:
        with engine.connect():
            logger.info("✅ Database connected successfully!")
    except Exception as e:
        logger.error(f"❌ Database connection failed: {e}")

# ✅ Register API routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(resume.router, prefix="/resumes", tags=["Resume Upload"])
app.include_router(scoring.router, prefix="/scoring", tags=["Resume Scoring"])
app.include_router(jobs.router, prefix="/api", tags=["Job Matching"])
app.include_router(job_application.router, prefix="/api/job_applications", tags=["Job Applications"])
app.include_router(dashboard.router, tags=["Dashboard"])  

@app.get("/")
def root():
    """Root endpoint for health check."""
    return {"message": "🚀 AI Resume Analyzer is running!"}
