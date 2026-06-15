from fastapi import FastAPI
from app.routers import gugus_checker

app = FastAPI(
    title="Backend GEREX 2026 - Gugus Checker",
    description="FastAPI backend untuk mengecek data gugus mahasiswa baru berdasarkan NRP.",
    version="1.0.0",
)

app.include_router(gugus_checker.router)


@app.get("/")
def root():
    return {
        "message": "Gugus Checker API",
        "usage": "Gunakan endpoint /{NRP}, contoh: /5027251066",
    }
