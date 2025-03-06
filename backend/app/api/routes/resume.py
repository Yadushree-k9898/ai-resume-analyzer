# import re
# import fitz
# import docx2txt
# import io
# from fastapi import UploadFile, HTTPException, APIRouter, File

# router = APIRouter()

# @router.post("/upload")
# async def upload_resume(file: UploadFile = File(...)):
#     """
#     Endpoint to upload a resume file (PDF or DOCX) and extract its text.
#     """
#     try:
#         filename = file.filename.lower()
#         if not filename.endswith((".pdf", ".docx")):
#             raise HTTPException(status_code=400, detail="Unsupported file format. Please upload a PDF or DOCX file.")

#         file_content = await file.read()

#         if filename.endswith(".pdf"):
#             with fitz.open(stream=io.BytesIO(file_content), filetype="pdf") as doc:
#                 text = "\n".join([page.get_text("text") for page in doc])
#         else:
#             text = docx2txt.process(io.BytesIO(file_content))

#         if not text.strip():
#             raise HTTPException(status_code=400, detail="No readable text found. Please upload a valid resume.")

#         # Cleaning extracted text
#         text = text.encode("utf-8", "ignore").decode("utf-8")  # Remove invalid characters
#         text = re.sub(r"[^\x20-\x7E]", " ", text)  # Remove non-printable ASCII characters
#         text = re.sub(r"\s+", " ", text).strip()  # Normalize spaces and new lines

#         return {"filename": file.filename, "extracted_text": text[:500]}  # Limiting response size for preview

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error processing resume: {str(e)}")



import re
import fitz
import docx2txt
import io
from fastapi import UploadFile, HTTPException, APIRouter, File

router = APIRouter()

def clean_text(text: str) -> str:
    text = text.encode("utf-8", "ignore").decode("utf-8")  # Remove invalid characters
    text = re.sub(r"[^\\x20-\\x7E]", " ", text)  # Remove non-printable ASCII characters
    text = re.sub(r"\\s+", " ", text).strip()  # Normalize spaces and new lines
    return text

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    """
    Endpoint to upload a resume file (PDF or DOCX) and extract its text.
    """
    try:
        filename = file.filename.lower()
        if not filename.endswith((".pdf", ".docx")):
            raise HTTPException(status_code=400, detail="Unsupported file format. Please upload a PDF or DOCX file.")

        file_content = await file.read()
        
        if filename.endswith(".pdf"):
            with fitz.open(stream=io.BytesIO(file_content), filetype="pdf") as doc:
                text = "\n".join([page.get_text("text") for page in doc])
        else:
            text = docx2txt.process(io.BytesIO(file_content))

        text = clean_text(text)
        if not text:
            raise HTTPException(status_code=400, detail="No readable text found. Please upload a valid resume.")

        return {"filename": file.filename, "extracted_text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing resume: {str(e)}")
