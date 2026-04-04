from pydantic import BaseModel
from model.estudante import Estudante

class EstudanteSchema(BaseModel):
    nome: str
    rank_universidade: int
    cgpa: float
    dsa_score: float
    coding_skills: float
    internships: int

class EstudanteViewSchema(BaseModel):
    id: int
    nome: str
    rank_universidade: int
    cgpa: float
    dsa_score: float
    coding_skills: float
    internships: int
    resultado: int = None

def apresenta_predicao(estudante: Estudante, predicao: int):
    return {
        'id': estudante.id,
        'nome': estudante.nome,
        'rank_universidade': estudante.rank_universidade,
        'cgpa': estudante.cgpa,
        'dsa_score': estudante.dsa_score,
        'coding_skills': estudante.coding_skills,
        'internships': estudante.internships,
        'resultado': predicao
    }