from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import pdfplumber  # PDF text extraction
import io
from app.services.resume_scorer import analyze_resume_quality

router = APIRouter()

@router.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    """Uploads a resume (PDF) and analyzes its content."""
    
    if not file:
        raise HTTPException(status_code=400, detail="File is required")
    
    try:
        # Read the uploaded file
        contents = await file.read()
        print(f"Received file: {file.filename}, Size: {len(contents)} bytes")  # Debugging

        # Extract text from PDF
        text = extract_text_from_pdf(contents)

        # Ensure text was extracted properly
        if not text.strip():
            raise HTTPException(status_code=400, detail="Could not extract text from the resume.")

        # Analyze resume quality
        analysis_result = analyze_resume_quality(text)

        return {"filename": file.filename, "extracted_text": text[:500], **analysis_result}  # Show first 500 chars for debugging

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract text from a PDF file using pdfplumber."""
    text = ""
    try:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting text from PDF: {str(e)}")

    return text.strip()
