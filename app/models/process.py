from typing import List, Optional, Union
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class FileSummary(BaseModel):
    filename: str
    summary: str

class ProcessResponse(BaseModel):
    request_id: UUID
    user_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now())
    query: Optional[str]
    result: Union[List[str], List[FileSummary]]
