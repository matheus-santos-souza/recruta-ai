from typing import List, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime
from app.models.chat import ChatOutput
from app.models.file_summary import FileSummary

class ProcessResponse(BaseModel):
    request_id: str
    user_id: str
    timestamp: datetime = Field(default_factory=datetime.now)
    query: Optional[str] = None
    result: Union[ChatOutput, List[FileSummary]]


