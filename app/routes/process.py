import json
from fastapi import APIRouter, UploadFile, File, Form, Request
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

from app.agents.recruiter_qa_agent import RecruiterQAAgent
from app.agents.curriculum_summarizer_agent import CurriculumSummarizerAgent
from app.models.chat import ChatOutput
from app.models.log import Log
from app.models.process import FileSummary, ProcessResponse
from app.repository.log_repository import save_log
from app.services.cache_summary_service import get_cache_summary, set_cache_summary
from app.services.ocr_service import OCRService

router = APIRouter(prefix="/api", tags=["Processamento de currículos"])

@router.post("/process", response_model=ProcessResponse)
async def process_documents(
    request: Request,
    files: List[UploadFile] = File(...),
    query: Optional[str] = Form(None),
    request_id: str = Form(...),
    user_id: str = Form(...)
):
    file_summaries: List[FileSummary] = []

    for file in files:
        file_content = await file.read()
        summary_cache = get_cache_summary(file_content)
        if summary_cache:
            summary = summary_cache
        else:
            extracted_text = OCRService.extract_text(file_content, file.filename)
            summary = CurriculumSummarizerAgent.run(extracted_text)
            set_cache_summary(file_content, summary)
        file_summaries.append(
            FileSummary(
                filename=file.filename,
                summary=summary
            )
        )

    if query:
        summaries = [fs.summary for fs in file_summaries]
        content = RecruiterQAAgent.run(query, summaries)
        result = ChatOutput(content=content)
    else:
        result = file_summaries

    if isinstance(result, BaseModel):
        resultado = result.model_dump_json()
    else:
        resultado = json.dumps([fs.dict() for fs in result])

    db = request.app.state.db
    await save_log(
        db=db,
        log=Log(
            query=query,
            request_id=request_id,
            user_id=user_id,
            resultado=resultado,
            timestamp=datetime.now()
        )
    )


    return ProcessResponse(
        request_id=request_id,
        user_id=user_id,
        timestamp=datetime.now(),
        query=query,
        result=result,
    )
