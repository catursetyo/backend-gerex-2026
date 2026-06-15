from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.gugus_checker import router as gugus_checker_router

app = FastAPI(
    title="Backend GEREX 2026 - Gugus Checker",
    description="FastAPI backend untuk mengecek data gugus mahasiswa baru berdasarkan NRP.",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Gugus Checker API is running"}


app.include_router(gugus_checker_router)
