import fitz  # PyMuPDF
import docx2txt
from fastapi import UploadFile, HTTPException

def extract_resume_text(file: UploadFile):
    """Extract text from uploaded resume file (PDF or DOCX)."""
    file_extension = file.filename.split(".")[-1].lower()

    if file_extension == "pdf":
        with fitz.open(stream=file.file.read(), filetype="pdf") as doc:
            text = "\n".join(page.get_text() for page in doc)
    elif file_extension == "docx":
        text = docx2txt.process(file.file)
    else:
        raise HTTPException(status_code=400, detail="Unsupported file format. Only PDF/DOCX allowed.")

    return text
