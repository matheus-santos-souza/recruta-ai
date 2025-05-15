from pydantic import BaseModel

class FileSummary(BaseModel):
  filename: str
  summary: str