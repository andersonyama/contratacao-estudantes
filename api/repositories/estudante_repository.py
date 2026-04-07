from db.session import Session
from model.estudante import Estudante

def insert_estudante(estudante: Estudante) -> Estudante:
    try:
        with Session() as session:
            session.add(estudante)
            session.commit()
            session.refresh(estudante)
        return estudante
    except Exception as e:
        raise e
    
def get_all_estudantes() -> list[Estudante]:
    try:
        with Session() as session:
            estudantes = session.query(Estudante).all()
        return estudantes
    except Exception as e:
        raise e
    
def delete_estudante(id: int):
    try:
        with Session() as session:
            estudante = session.get(Estudante, id)
            if estudante:
                session.delete(estudante)
                session.commit()
            else:
                raise Exception("Registro não encontrado")
    except Exception as e:
        raise e