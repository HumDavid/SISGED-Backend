from fastapi import APIRouter
from . import service
from .schemas import CursoOut

router = APIRouter(prefix="/cursos", tags=["Cursos"])

@router.get("", response_model=list[CursoOut])
def listarCursos():
    return service.listarCursos()