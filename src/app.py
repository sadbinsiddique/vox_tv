import os 
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from src.routes import (
    auth
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

uploaded_dir = "uploads"
os.makedirs(uploaded_dir, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=uploaded_dir), name="uploads")

# Include routers
app.include_router(auth.router)


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Vox TV API",
        "version": "0.1.0",
        "status": "running",
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
