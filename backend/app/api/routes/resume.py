# from fastapi import APIRouter, UploadFile, File, HTTPException
# from app.api.routes import auth, resume

# import fitz  # PyMuPDF for PDF parsing
# import docx2txt

# router = APIRouter()

# def extract_text(file: UploadFile):
#     if file.filename.endswith(".pdf"):
#         doc = fitz.open(stream=file.file.read(), filetype="pdf")
#         text = "\n".join([page.get_text("text") for page in doc])
#     elif file.filename.endswith(".docx"):
#         text = docx2txt.process(file.file)
#     else:
#         raise HTTPException(status_code=400, detail="Unsupported file format")
#     return text

# @router.post("/upload")
# async def upload_resume(file: UploadFile = File(...)):
#     text = extract_text(file)
#     return {"message": "Resume processed", "extracted_text": text}



from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.core.auth import get_current_user
import fitz  # PyMuPDF for PDF parsing
import docx2txt
import io

router = APIRouter()

def extract_text(file: UploadFile):
    try:
        file_content = file.file.read()  # Read the file into memory
        if file.filename.endswith(".pdf"):
            doc = fitz.open(stream=io.BytesIO(file_content), filetype="pdf")
            text = "\n".join([page.get_text("text") for page in doc])
        elif file.filename.endswith(".docx"):
            text = docx2txt.process(io.BytesIO(file_content))
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format")
        
        if not text.strip():  # Check if text is empty
            raise HTTPException(status_code=400, detail="No text extracted. Please upload a valid resume.")

        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing resume: {str(e)}")

@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    current_user: dict = Depends(get_current_user)  # Ensure user authentication
):
    text = extract_text(file)
    return {
        "message": "Resume processed successfully",
        "extracted_text": text,
        "uploaded_by": current_user["email"],  # Return user info
    }
