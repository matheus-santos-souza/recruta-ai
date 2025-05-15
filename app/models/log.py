from pydantic import BaseModel
from datetime import datetime

class Log(BaseModel):
  request_id: str
  user_id: str
  timestamp: datetime
  query: str
  resultado: str
