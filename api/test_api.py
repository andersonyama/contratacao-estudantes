import pytest
import json
from app import app

@pytest.fixture
def client():
    """Configura o cliente de teste para a aplicação Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def estudante_teste():
    """Dados de exemplo para teste de estudante"""
    return {
        'rank_universidade': 2,
        'cgpa': 8,
        'dsa_score': 8,
        'coding_skills': 8,
        'internships': 1,
    }

def teste_redirect_home(client):
    response = client.get('/')
    assert response.status_code == 302
    assert '/openapi/swagger' in response.location

def teste_predicao_estudante(client, estudante_teste):
    response = client.post('/estudante',
                           data=json.dumps(estudante_teste),
                           content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)

    assert 'resultado' in data
    assert data['resultado'] in [0,1]