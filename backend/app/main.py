from fastapi import FastAPI

from app.database.database import engine
from app.database.base import Base

import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Resume Screening System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Resume Screening System"
    }


@app.get("/health")
def health():
    return {
        "status": "Running"
    }