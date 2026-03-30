import numpy as np

class Estudante():

    def __init__(self, rank_universidade:int,
                 cgpa:float, coding_skills:float,
                 dsa_score:float, internships:int):
        self.rank_universidade = rank_universidade
        self.cgpa = cgpa
        self.dsa_score = dsa_score
        self.coding_skills = coding_skills
        self.internships = internships

    def vetor_atributos(self):
        vetor = np.array([self.rank_universidade, self.cgpa, self.dsa_score, self.coding_skills, self.internships])
        vetor = vetor.reshape(1, -1)
        return vetor