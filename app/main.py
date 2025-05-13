from fastapi import FastAPI
from app.routes import process

app = FastAPI(
  title="Recruta AI - API",
  description="Ferramenta inteligente para processar currículos com OCR e LLM.",
  version="0.1.0"
)

app.include_router(process.router)