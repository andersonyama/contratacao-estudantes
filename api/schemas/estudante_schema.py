from pydantic import BaseModel
from model.estudante import Estudante

class EstudanteRequest(BaseModel):
    nome: str
    rank_universidade: int
    cgpa: float
    dsa_score: float
    coding_skills: float
    internships: int

class EstudanteResponse(BaseModel):
    id: int
    nome: str
    rank_universidade: int
    cgpa: float
    dsa_score: float
    coding_skills: float
    internships: int
    resultado: int = None

class EstudanteListResponse(BaseModel):
    estudantes: list[EstudanteResponse]

def apresenta_predicao(estudante: Estudante):
    return {
        'id': estudante.id,
        'nome': estudante.nome,
        'rank_universidade': estudante.rank_universidade,
        'cgpa': estudante.cgpa,
        'dsa_score': estudante.dsa_score,
        'coding_skills': estudante.coding_skills,
        'internships': estudante.internships,
        'resultado': estudante.predicao
    }

def apresenta_lista_predicao(estudantes: list[Estudante]):
    return {
        'estudantes': [apresenta_predicao(estudante) for estudante in estudantes]
    }