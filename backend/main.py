from fastapi import FastAPI

app = FastAPI(
    title="AI Resume Screening System",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Resume Screening System"
    }

@app.get("/health")
def health():
    return {
        "status": "Server Running Successfully"
    }