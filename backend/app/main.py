from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, resume  # Importing resume routes
from app.core.database import Base, engine

# Initialize FastAPI app
app = FastAPI(debug=True)

# CORS Middleware (Update allow_origins with frontend URL if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific origins for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Function to create tables
def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully!")
    except Exception as e:
        print(f"❌ Error creating tables: {e}")

# Run tasks on startup
@app.on_event("startup")
def startup_event():
    print("🚀 Starting AI Resume Analyzer Backend...")
    create_tables()
    try:
        with engine.connect() as conn:
            print("✅ Database connected successfully!")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")

# Include authentication routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

# Include resume routes
app.include_router(resume.router, prefix="/resumes", tags=["Resumes"])  # Ensure resume routes are included

@app.get("/")
def root():
    return {"message": "🚀 AI Resume Analyzer is running!"}
