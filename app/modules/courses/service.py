from . import repository
def listarCursos() -> list[dict]:
    return sorted(repository)