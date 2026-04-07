from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS

from schemas import *
from model import *
from repositories import *
from db.session import init_db

init_db()

info = Info(title="Contratação Estudantes", version="1.0.0")
app = OpenAPI(
    __name__,
    info=info,
    static_folder='../front_end'
)
CORS(app)

home_tag = Tag(name='Documentação', description='Página inicial da documentação')
estudante_tag = Tag(name='Estudante', description='Predição de contratação de formandos')

# rota home encaminha para o front-end
@app.get('/')
def home():
    return redirect('front_end/index.html')

# rota docs encaminha para documentação no swagger
@app.get('/docs', tags=[home_tag])
def docs():
    return redirect('/openapi/swagger')

@app.post(
    '/estudante',
    tags=[estudante_tag],
    responses={
        '200': EstudanteResponse
    }
)
def previsor_contratacao(body: EstudanteRequest):
    estudante = Estudante(
        body.nome,
        body.rank_universidade,
        body.cgpa,
        body.dsa_score,
        body.coding_skills,
        body.internships
    )

    modelo = Modelo()

    path_modelo = "modelagem/modelo_contratacao_estudantes.pkl"
    modelo.carrega_modelo(path_modelo)
    estudante.predicao = int(modelo.preditor(estudante.exporta_df())[0])
    insert_estudante(estudante)
    
    return apresenta_predicao(estudante), 200

@app.get('/estudante',
    tags=[estudante_tag],
    responses={
        '200': EstudanteListResponse
    }
)
def lista_resultados():
    try:
        estudantes = get_all_estudantes()
        return apresenta_lista_predicao(estudantes), 200
    except Exception as e:
        return {'message': 'Erro ao listar os ativos.'}, 400