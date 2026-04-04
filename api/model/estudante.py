from datetime import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Union

import numpy as np

from model import Base

class Estudante(Base):
    __tablename__ = 'estudantes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    rank_universidade: Mapped[int] = mapped_column(nullable=False)
    cgpa: Mapped[float] = mapped_column(nullable=False)
    dsa_score: Mapped[float] = mapped_column(nullable=False)
    coding_skills: Mapped[float] = mapped_column(nullable=False)
    internships: Mapped[int] = mapped_column(nullable=False)
    predicao: Mapped[int] = mapped_column(nullable=False)
    data_predicao: Mapped[datetime] = mapped_column(nullable=False, default= datetime.now())

    def __init__(self, nome:str, rank_universidade:int,
                 cgpa:float, coding_skills:float,
                 dsa_score:float, internships:int,
                 data_predicao:Union[datetime, None] = None):
        self.nome = nome
        self.rank_universidade = rank_universidade
        self.cgpa = cgpa
        self.dsa_score = dsa_score
        self.coding_skills = coding_skills
        self.internships = internships

        if data_predicao:
            self.data_predicao = data_predicao

    def vetor_atributos(self):
        vetor = np.array([self.rank_universidade, self.cgpa, self.dsa_score, self.coding_skills, self.internships])
        vetor = vetor.reshape(1, -1)
        return vetor