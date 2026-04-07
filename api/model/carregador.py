import pandas as pd

class Carregador:

    def __init__(self):
        pass

    def carregar_dados(self, url_dados: str, atributos_modelo: list):
        '''Carrega dados do arquivo disponível na url_informado, com tratamento inicial de dados, selecionando atributos informados

        Arguments:
        url_dados: caminho do arquivo de dados
        atributos_modelo: lista de atributos a serem utilizados'''
        
        labels = ['ramo', 'rank_universidade', 'cgpa', 'reprovacoes', 'coding_skills',
       'dsa_score', 'aptitude_score', 'communication_skills', 'ml_knowledge',
       'system_design', 'internships', 'projects_count', 'certifications',
       'hackathons', 'open_source_contributions', 'extracurriculars',
       'contratado','salario']
        df_estudantes = pd.read_csv(url_dados, names=labels, header=0)
        df_estudantes['rank_universidade'] = df_estudantes['rank_universidade'].str.slice(5,6).astype(int)

        return df_estudantes[atributos_modelo]

