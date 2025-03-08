import re
import fitz  # PyMuPDF for PDF parsing
import docx2txt
import io
from fastapi import UploadFile, HTTPException, APIRouter, File

router = APIRouter()

# Maximum allowed file size (2MB)
MAX_FILE_SIZE_MB = 2

def clean_text(text: str) -> str:
    """Clean extracted resume text."""
    text = text.encode("utf-8", "ignore").decode("utf-8")  # Remove invalid characters
    text = re.sub(r"[^\x20-\x7E]", " ", text)  # Remove non-printable ASCII characters
    text = re.sub(r"\s+", " ", text).strip()  # Normalize spaces and new lines
    return text

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    """Upload a resume (PDF or DOCX) and extract text."""
    try:
        filename = file.filename.lower()
        
        # ✅ Validate file type
        if not filename.endswith((".pdf", ".docx")):
            raise HTTPException(status_code=400, detail="Unsupported file format. Please upload a PDF or DOCX file.")

        file_content = await file.read()

        # ✅ Validate file size
        if len(file_content) > MAX_FILE_SIZE_MB * 1024 * 1024:
            raise HTTPException(status_code=400, detail=f"File is too large. Max allowed size is {MAX_FILE_SIZE_MB}MB.")

        # ✅ Extract text
        if filename.endswith(".pdf"):
            with fitz.open(stream=io.BytesIO(file_content), filetype="pdf") as doc:
                text = "\n".join([page.get_text("text") for page in doc])
        else:
            text = docx2txt.process(io.BytesIO(file_content))

        text = clean_text(text)

        # ✅ Check if extracted text is empty
        if not text:
            raise HTTPException(status_code=400, detail="No readable text found. Please upload a valid resume.")

        return {"filename": file.filename, "extracted_text": text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing resume: {str(e)}")
