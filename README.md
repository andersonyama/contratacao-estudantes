# contratacao-estudantes

## Descrição do Projeto

Este projeto consiste no desenvolvimento de uma aplicação full-stack que utiliza um modelo de ML de categorização para a predição da contratação de um graduando no mercado de trabalho..

A aplicação foi desenvolvida como parte do MVP do módulo de **Qualidade de Software, Segurança e Sistemas Inteligentes** do  curso de **Pós-Graduação em Engenharia de Software da PUC-RIO**, com o objetivo de aplicar modelos de Machine Learning para construção de aplicações, além da verificação de qualidade através de testes automatizados.

---

## Funcionalidade

- Predição de contratação de graduandos e armazenamento de resultados

---

## Estrutura do Projeto

```text
contratacao-estudantes/
│
├── api/
│   ├── app.py                          # ponto de boot da aplicação
│   ├── db/                             # engine, Session e inicializador do banco de dados
│   ├── model/                          # classes dos modelos utilizados
│   ├── repositories/                   # classes de interação com o banco de dados
│   ├── schemas/                        # schemas de interação com os endpoints
│   ├── test_api.py                     # teste automatizado da aplicação
│   └── test_modelo.py                  # teste de validação do modelo utilizado
├── database/                           # arquivo sqlite (ignorado pelo git)
├── front_end/                          # front-end da aplicação
└── modelagem/                          
    ├── modelagem_contratacao_estudantes.ipynb         # construção do modelo de ML
    ├── modelo_contratacao_estudantes.pkl              # modelo empacotado para uso pela aplicação
    └── student-placement-dataset.zip                  # arquivo base do modelo
```

---

## Tecnologias Utilizadas

- Python (recomendado: 3.9+)
- Flask (API)
- flask-openapi3 (documentação OpenAPI/Swagger)
- flask-cors (CORS)
- SQLAlchemy (ORM)
- SQLite (banco local)
- Pydantic (validação / schemas)
- pip (gerenciador de pacotes)
- pytest (framework de testes)
- scikit-learn (modelagem de ML)

Dependências do projeto estão listadas em [requirements.txt](api/requirements.txt).

---

## Requisitos

- Python 3.9 ou superior (instale via python.org / pyenv)
- pip
- (recomendado) uso de ambiente virtual: venv ou virtualenv
- Permissão de escrita para criar o diretório `database/` (o arquivo SQLite é criado neste diretório por [`api/db/session.py`](api/db/session.py))

---


## Instalação

```bash
python -m venv .venv
# ative o venv:
# Linux/macOS: source 
.venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## Inicialização

Exemplo usando flask CLI apontando para o package:

```bash
set FLASK_APP=api/app.py       # Windows CMD
flask run --host 0.0.0.0 --port 5000
```

A documentação Swagger estará disponível em:
http://localhost:5000/docs

A aplicação estará disponibilizada em: http://localhost:5000/

Para execução dos testes:

```bash
pytest -v api/test_api.py
pytest -v api/test_modelo.py
```

--- 

## Contexto Acadêmico

Projeto desenvolvido para fins acadêmicos no curso de Pós-Graduação em Engenharia de Software da PUC-RIO.