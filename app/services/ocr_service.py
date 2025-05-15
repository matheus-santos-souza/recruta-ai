from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes
import io

class OCRService:
    @staticmethod
    def extract_text(file_bytes: bytes, filename: str) -> str:
        if filename.endswith(".pdf"):
            images = convert_from_bytes(file_bytes)
            text = "\n".join(pytesseract.image_to_string(img) for img in images)
        else:
            image = Image.open(io.BytesIO(file_bytes))
            text = pytesseract.image_to_string(image)
        return text
