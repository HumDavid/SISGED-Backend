from uuid import UUID

_CURSOS = [
    {"id": UUID(int=1), "nome": "Ciência da Computação"},
    {"id": UUID(int=2), "nome": "Sistemas de Informação"},
]
def listarCursos()-> list[dict]:
    return _CURSOS