from model import *

carregador = Carregador()
modelo = Modelo()
avaliador = Avaliador()

url_dados = 'modelagem/student-placement-dataset.zip'
atributos_modelo = ['rank_universidade','cgpa','coding_skills','dsa_score','internships', 'contratado']

dados = carregador.carregar_dados(url_dados, atributos_modelo)
X = dados[atributos_modelo[:-1]]
Y = dados[atributos_modelo[-1]]

def test_modelo():
    path_modelo = "modelagem/modelo_contratacao_estudantes.pkl"
    modelo_teste = modelo.carrega_modelo(path_modelo)
    acuracia = avaliador.avaliar_modelo(modelo_teste, X, Y)

    assert acuracia >= 0.65