from fastapi import APIRouter, UploadFile, File, Form
from typing import List, Optional
from uuid import UUID
from app.models.process import ProcessResponse
from datetime import datetime
from app.services.ocr_service import OCRService
from app.agents.summarizer import Summarizer

router = APIRouter(prefix="/api", tags=["Processamento de Currículos"])

@router.post("/process", response_model=ProcessResponse)
async def process_documents(
    files: List[UploadFile] = File(...),
    query: Optional[str] = Form(None),
    request_id: UUID = Form(...),
    user_id: str = Form(...)
):
    summarizers_files = []

    for file in files:
        contents = await file.read()
        text = OCRService.extract_text(contents, file.filename)
        summary = Summarizer.summarize(text)
        summarizers_files.append({
            "filename": file.filename,
            "summary": summary
        })

    results = []
    if query:
        results.append("Query response LLM")
    else:
        results=summarizers_files

    return ProcessResponse(
        request_id=request_id,
        user_id=user_id,
        timestamp=datetime.now(),
        query=query,
        result=results,
    )
