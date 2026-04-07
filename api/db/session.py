"""
Configuração da base de dados e de sessão
"""

from pathlib import Path
import logging

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from model.base import Base

# Configuração do logger
logger = logging.getLogger(__name__)
if not logger.handlers:
    logging.basicConfig(level=logging.INFO)

# Criação do diretório para o banco de dados, se necessário
project_root = Path(__file__).resolve().parents[2]
DB_DIR = project_root / "database"
DB_DIR.mkdir(parents=True, exist_ok=True)
logger.info("Diretório para criação de tabelas disponível: %s", DB_DIR)

# Criação engine
_db_file = DB_DIR / "estudantes.sqlite3"
db_url: str = f"sqlite:///{_db_file.as_posix()}"
engine: Engine = create_engine(db_url, echo=False)

# Configuração de criador de seção
Session = sessionmaker(bind=engine)

def init_db(create: bool = True) -> None:
    """Criação de tabelas no banco de dados

    Arguments:
        create: se True, cria tabelas
    """
    if create:
        Base.metadata.create_all(engine)
        logger.info("Banco de dados inicializado em %s", db_url)