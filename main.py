from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pathlib import Path
from fastapi.staticfiles import StaticFiles

from api.router.agent import router as agent_router

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# from src.config.config import UPLOAD_DIR
# app.mount("/files", StaticFiles(directory=Path(UPLOAD_DIR)), name="files")

@app.get("/")
async def root():
    return {"message": "Hello IsDBI!"}

app.include_router(agent_router, prefix="/agent", tags=["Agent"])
