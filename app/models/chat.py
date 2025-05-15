from enum import Enum
from pydantic import BaseModel

class Role(str, Enum):
    user = "user"
    assistant = "assistant"
    system = "system"

class Chat(BaseModel):
  role: Role
  content: str

class ChatOutput(BaseModel):
  content: str

class ChatThinkingOutput(BaseModel):
  thinking_content: str
  content: str