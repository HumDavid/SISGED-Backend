from uuid import UUID
from pydantic import BaseModel

class CursoOut(BaseModel):
    id: UUID
    nome: str