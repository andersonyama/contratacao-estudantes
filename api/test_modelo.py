from model import *

# para executar o teste: pytest -v api/test_modelo.py

carregador = Carregador()
modelo = Modelo()
avaliador = Avaliador()

# parâmetros selecionados
atributos_modelo = ['rank_universidade','cgpa','coding_skills','dsa_score','internships', 'contratado']

# carga dos dados
url_dados = 'modelagem/student-placement-dataset.zip'
dados = carregador.carregar_dados(url_dados, atributos_modelo)
X = dados[atributos_modelo[:-1]]
Y = dados[atributos_modelo[-1]]

def teste_modelo():
    """Teste do modelo carregado"""
    path_modelo = "modelagem/modelo_contratacao_estudantes.pkl"
    modelo_teste = modelo.carrega_modelo(path_modelo)
    acuracia = avaliador.avaliar_modelo(modelo_teste, X, Y)

    assert acuracia >= 0.65