from fastapi import FastAPI

from app.database.database import Base, engine
from app.models import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Resume Screening System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Resume Screening System API"
    }


@app.get("/health")
def health():
    return {
        "status": "Running"
    }