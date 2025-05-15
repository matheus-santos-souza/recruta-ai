from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.mongo import lifespan
from app.routes import process

app = FastAPI(
  title="Recruta AI - API",
  description="Ferramenta inteligente para processar currículos com OCR e LLM.",
  version="0.1.0",
  lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(process.router)