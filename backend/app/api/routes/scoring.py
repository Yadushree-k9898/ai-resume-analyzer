from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi import APIRouter


router = APIRouter()

@router.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    try:
        # Read the file as bytes instead of trying to decode it as text
        contents = await file.read()

        # Process the file here (if it's a PDF, use pdfplumber or PyMuPDF)
        # Example: Save file for debugging
        with open(f"temp_{file.filename}", "wb") as f:
            f.write(contents)

        return {"message": "File received successfully", "filename": file.filename}
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
