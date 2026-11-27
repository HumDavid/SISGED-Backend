from fastapi import FastAPI
from app.modules.courses.router import router as cursos_router

app = FastAPI(title="Sisgedi API")
app.include_router(cursos_router, prefix="/api/v1")