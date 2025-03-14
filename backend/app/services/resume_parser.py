
# import fitz  # PyMuPDF
# import docx2txt
# import io
# import re
# import unicodedata
# from fastapi import HTTPException
# from sqlalchemy.orm import Session
# from app.models.resume import Resume
# from app.services.resume_analyzer import analyze_resume_quality_service


# def clean_text(text: str) -> str:
#     """Cleans extracted resume text to remove corruption."""
#     try:
#         text = text.encode("utf-8", "ignore").decode("utf-8")  # Remove invalid characters
#         text = unicodedata.normalize("NFKC", text)  # Normalize Unicode characters
#         text = re.sub(r"[^\x20-\x7E]", " ", text)  # Remove non-printable characters
#         text = re.sub(r"\s+", " ", text).strip()  # Normalize spaces
#         return text
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error cleaning text: {str(e)}")

# def extract_resume_text(file_content: bytes, file_extension: str) -> str:
#     """Extracts and cleans text from a resume file."""
#     try:
#         text = ""
#         if file_extension == "pdf":
#             with fitz.open(stream=io.BytesIO(file_content), filetype="pdf") as doc:
#                 text = "\n".join([page.get_text("text") for page in doc])  # Extract text from each page
#         elif file_extension == "docx":
#             text = docx2txt.process(io.BytesIO(file_content))
#         else:
#             raise HTTPException(status_code=400, detail="Unsupported file format. Only PDF/DOCX allowed.")

#         if not text.strip():
#             raise HTTPException(status_code=400, detail="No readable text found in the resume.")

#         return clean_text(text)
    
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error extracting resume text: {str(e)}")

# def save_resume(user_id: int, file_path: str, extracted_text: str, db: Session):
#     """Extracts skills, identifies missing skills, and saves resume details."""
#     try:
#         extracted_skills, missing_skills = analyze_resume_quality_service(extracted_text)

#         print(f"DEBUG: Extracted skills = {extracted_skills}")  # ✅ Debugging line

#         new_resume = Resume(
#             user_id=user_id,
#             file_path=file_path,  # ✅ Ensure file_path is stored
#             extracted_text=extracted_text,
#             skills=extracted_skills,  # ✅ Store as JSONB (list)
#             missing_skills=missing_skills if missing_skills else []
#         )
#         db.add(new_resume)
#         db.commit()
#         db.refresh(new_resume)

#         return new_resume  # ✅ Return saved resume for debugging
    
#     except Exception as e:
#         db.rollback()
#         raise HTTPException(status_code=500, detail=f"Error saving resume: {str(e)}")



import fitz  # PyMuPDF
import docx2txt
import io
import re
import unicodedata
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.resume import Resume
from app.services.resume_analyzer import analyze_resume_quality_service


def clean_text(text: str) -> str:
    """Cleans extracted resume text to remove corruption."""
    try:
        text = text.encode("utf-8", "ignore").decode("utf-8")  # Remove invalid characters
        text = unicodedata.normalize("NFKC", text)  # Normalize Unicode characters
        text = re.sub(r"[^\x20-\x7E]", " ", text)  # Remove non-printable characters
        text = re.sub(r"\s+", " ", text).strip()  # Normalize spaces
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error cleaning text: {str(e)}")


# def extract_resume_text(file_content: bytes, file_extension: str) -> str:
#     """Extracts and cleans text from a resume file."""
#     try:
#         text = ""
#         if file_extension == "pdf":
#             with fitz.open(stream=io.BytesIO(file_content), filetype="pdf") as doc:
#                 text = "\n".join([page.get_text("text") for page in doc])  # Extract text from each page
#         elif file_extension == "docx":
#             text = docx2txt.process(io.BytesIO(file_content))
#         else:
#             raise HTTPException(status_code=400, detail="Unsupported file format. Only PDF/DOCX allowed.")

#         if not text.strip():
#             raise HTTPException(status_code=400, detail="No readable text found in the resume.")

#         return clean_text(text)

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error extracting resume text: {str(e)}")
def extract_resume_text(file_content: bytes, file_extension: str) -> str:
    """Extracts and cleans text from a resume file."""
    try:
        text = ""
        if file_extension == "pdf":
            with fitz.open(stream=io.BytesIO(file_content), filetype="pdf") as doc:
                text = "\n".join([page.get_text("text") for page in doc])  # Extract text from each page
        elif file_extension == "docx":
            text = docx2txt.process(io.BytesIO(file_content))
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format. Only PDF/DOCX allowed.")

        if not text.strip():
            raise HTTPException(status_code=400, detail="No readable text found in the resume.")

        print(f"DEBUG: Extracted Resume Text (First 500 chars):\n{text[:500]}")  # ✅ Print first 500 chars

        return clean_text(text)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting resume text: {str(e)}")


# def save_resume(user_id: int, file_path: str, extracted_text: str, db: Session):
#     """Extracts skills and saves resume details."""
#     try:
#         extracted_skills = analyze_resume_quality_service(extracted_text)

#         # ✅ Ensure extracted_skills is always a list
#         extracted_skills = extracted_skills if isinstance(extracted_skills, list) else []

#         print(f"DEBUG: Extracted skills = {extracted_skills}")  # ✅ Debugging line

#         # ✅ Prevent saving resume if no skills are extracted
#         if not extracted_skills:
#             raise HTTPException(status_code=400, detail="Resume must have at least one recognized skill.")

#         new_resume = Resume(
#             user_id=user_id,
#             file_path=file_path,  # ✅ Ensure file_path is stored
#             extracted_text=extracted_text,
#             skills=extracted_skills  # ✅ Store as JSONB (list)
#         )
#         db.add(new_resume)
#         db.commit()
#         db.refresh(new_resume)

#         return new_resume  # ✅ Return saved resume for debugging

#     except Exception as e:
#         db.rollback()
#         raise HTTPException(status_code=500, detail=f"Error saving resume: {str(e)}")
def save_resume(user_id: int, file_path: str, extracted_text: str, db: Session):
    """Extracts skills and saves resume details."""
    try:
        extracted_skills = analyze_resume_quality_service(extracted_text)

        print(f"DEBUG: Extracted Skills = {extracted_skills}")  # ✅ Print extracted skills

        if not extracted_skills:
            raise HTTPException(status_code=400, detail="Resume must have at least one recognized skill.")

        new_resume = Resume(
            user_id=user_id,
            file_path=file_path,
            extracted_text=extracted_text,
            skills=extracted_skills
        )
        db.add(new_resume)
        db.commit()
        db.refresh(new_resume)

        return new_resume  
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error saving resume: {str(e)}")
