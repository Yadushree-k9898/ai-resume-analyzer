# import re
# import fitz  # PyMuPDF for PDF parsing
# import docx2txt
# import io
# from fastapi import UploadFile, HTTPException, APIRouter, File

# router = APIRouter()

# # Maximum allowed file size (2MB)
# MAX_FILE_SIZE_MB = 2

# def clean_text(text: str) -> str:
#     """Clean extracted resume text."""
#     text = text.encode("utf-8", "ignore").decode("utf-8")  # Remove invalid characters
#     text = re.sub(r"[^\x20-\x7E]", " ", text)  # Remove non-printable ASCII characters
#     text = re.sub(r"\s+", " ", text).strip()  # Normalize spaces and new lines
#     return text

# @router.post("/upload")
# async def upload_resume(file: UploadFile = File(...)):
#     """Upload a resume (PDF or DOCX) and extract text."""
#     try:
#         filename = file.filename.lower()
        
#         # ✅ Validate file type
#         if not filename.endswith((".pdf", ".docx")):
#             raise HTTPException(status_code=400, detail="Unsupported file format. Please upload a PDF or DOCX file.")

#         file_content = await file.read()

#         # ✅ Validate file size
#         if len(file_content) > MAX_FILE_SIZE_MB * 1024 * 1024:
#             raise HTTPException(status_code=400, detail=f"File is too large. Max allowed size is {MAX_FILE_SIZE_MB}MB.")

#         # ✅ Extract text
#         if filename.endswith(".pdf"):
#             with fitz.open(stream=io.BytesIO(file_content), filetype="pdf") as doc:
#                 text = "\n".join([page.get_text("text") for page in doc])
#         else:
#             text = docx2txt.process(io.BytesIO(file_content))

#         text = clean_text(text)

#         # ✅ Check if extracted text is empty
#         if not text:
#             raise HTTPException(status_code=400, detail="No readable text found. Please upload a valid resume.")

#         return {"filename": file.filename, "extracted_text": text}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error processing resume: {str(e)}")



# import re
# import fitz  # PyMuPDF for PDF parsing
# import docx2txt
# import io
# from fastapi import UploadFile, HTTPException, APIRouter, File, Depends
# from sqlalchemy.orm import Session
# from app.core.database import get_db
# from app.services.resume_parser import extract_resume_text, save_resume

# router = APIRouter()

# # Maximum allowed file size (2MB)
# MAX_FILE_SIZE_MB = 2

# def clean_text(text: str) -> str:
#     """Clean extracted resume text."""
#     text = text.encode("utf-8", "ignore").decode("utf-8")  # Remove invalid characters
#     text = re.sub(r"[^\x20-\x7E]", " ", text)  # Remove non-printable ASCII characters
#     text = re.sub(r"\s+", " ", text).strip()  # Normalize spaces and new lines
#     return text

# @router.post("/upload")
# async def upload_resume(file: UploadFile = File(...), db: Session = Depends(get_db)):
#     """Upload a resume (PDF or DOCX) and extract text."""
#     try:
#         filename = file.filename.lower()
        
#         # ✅ Validate file type
#         if not filename.endswith((".pdf", ".docx")):
#             raise HTTPException(status_code=400, detail="Unsupported file format. Please upload a PDF or DOCX file.")

#         file_content = await file.read()

#         # ✅ Validate file size
#         if len(file_content) > MAX_FILE_SIZE_MB * 1024 * 1024:
#             raise HTTPException(status_code=400, detail=f"File is too large. Max allowed size is {MAX_FILE_SIZE_MB}MB.")

#         # ✅ Extract text
#         file_extension = "pdf" if filename.endswith(".pdf") else "docx"
#         extracted_text = extract_resume_text(file_content, file_extension)

#         # ✅ Check if extracted text is empty
#         if not extracted_text:
#             raise HTTPException(status_code=400, detail="No readable text found. Please upload a valid resume.")

#         # ✅ Save resume
#         save_resume(user_id=1, extracted_text=extracted_text, db=db)

#         return {"filename": file.filename, "extracted_text": extracted_text}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error processing resume: {str(e)}")


import os
import re
import fitz  # PyMuPDF for PDF parsing
import docx2txt
import io
from fastapi import UploadFile, HTTPException, APIRouter, File, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.resume_parser import extract_resume_text, save_resume

router = APIRouter()

# Maximum allowed file size (2MB)
MAX_FILE_SIZE_MB = 2
UPLOAD_DIR = "uploads"  # Directory to save uploaded resumes

# Ensure upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

def clean_text(text: str) -> str:
    """Clean extracted resume text."""
    text = text.encode("utf-8", "ignore").decode("utf-8")  # Remove invalid characters
    text = re.sub(r"[^\x20-\x7E]", " ", text)  # Remove non-printable ASCII characters
    text = re.sub(r"\s+", " ", text).strip()  # Normalize spaces and new lines
    return text

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Upload a resume (PDF or DOCX), save it, and extract text."""
    try:
        filename = file.filename.lower()

        # ✅ Validate file type
        if not filename.endswith((".pdf", ".docx")):
            raise HTTPException(status_code=400, detail="Unsupported file format. Please upload a PDF or DOCX file.")

        file_content = await file.read()

        # ✅ Validate file size
        if len(file_content) > MAX_FILE_SIZE_MB * 1024 * 1024:
            raise HTTPException(status_code=400, detail=f"File is too large. Max allowed size is {MAX_FILE_SIZE_MB}MB.")

        # ✅ Save the file locally
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as f:
            f.write(file_content)

        # ✅ Extract text
        file_extension = "pdf" if filename.endswith(".pdf") else "docx"
        extracted_text = extract_resume_text(file_content, file_extension)

        # ✅ Check if extracted text is empty
        if not extracted_text:
            raise HTTPException(status_code=400, detail="No readable text found. Please upload a valid resume.")

        # ✅ Save resume with file path (Fix: added `file_path`)
        save_resume(user_id=1, file_path=file_path, extracted_text=extracted_text, db=db)

        return {"filename": file.filename, "file_path": file_path, "extracted_text": extracted_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing resume: {str(e)}")
