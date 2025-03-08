
# import fitz  # PyMuPDF for PDFs
# import docx2txt  # For DOCX files
# import io
# import re
# import unicodedata
# from fastapi import HTTPException

# def clean_text(text: str) -> str:
#     """Cleans extracted resume text."""
#     try:
#         text = text.encode("utf-8", "ignore").decode("utf-8")  # Remove invalid characters
#         text = unicodedata.normalize("NFKC", text)  # Normalize Unicode characters
#         text = re.sub(r"[^\x20-\x7E]", " ", text)  # Remove non-printable ASCII characters
#         text = re.sub(r"\s+", " ", text).strip()  # Normalize spaces and new lines
#         return text
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error cleaning text: {str(e)}")

# def extract_resume_text(file_content: bytes, file_extension: str) -> str:
#     """Extracts and cleans text from a resume file."""
#     try:
#         text = ""
#         if file_extension == "pdf":
#             with fitz.open(stream=io.BytesIO(file_content), filetype="pdf") as doc:
#                 text = "\n".join([page.get_text("text_with_spaces") for page in doc])
#         elif file_extension == "docx":
#             text = docx2txt.process(io.BytesIO(file_content))
#         else:
#             raise HTTPException(status_code=400, detail="Unsupported file format. Only PDF/DOCX allowed.")

#         if not text.strip():
#             raise HTTPException(status_code=400, detail="No readable text found in the resume.")
        
#         return clean_text(text)
    
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error extracting resume text: {str(e)}")



import fitz  # PyMuPDF
import docx2txt
import io
import re
import unicodedata
from fastapi import HTTPException

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

def extract_resume_text(file_content: bytes, file_extension: str) -> str:
    """Extracts and cleans text from a resume file."""
    try:
        text = ""
        if file_extension == "pdf":
            with fitz.open(stream=io.BytesIO(file_content), filetype="pdf") as doc:
                text = "\n".join([page.get_text("text") for page in doc])  # Changed extraction method
        elif file_extension == "docx":
            text = docx2txt.process(io.BytesIO(file_content))
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format. Only PDF/DOCX allowed.")

        if not text.strip():
            raise HTTPException(status_code=400, detail="No readable text found in the resume.")

        return clean_text(text)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting resume text: {str(e)}")
