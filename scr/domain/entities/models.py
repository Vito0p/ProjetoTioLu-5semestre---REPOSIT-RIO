from sqlalchemy import Column, Integer, String, BLOB
from scr.infra.database import Base

# Modelo de Funcionário
class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(14), unique=True, index=True, nullable=False)
    senha = Column(String(200), nullable=False)

# Modelo de Cliente
class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(14), unique=True, index=True, nullable=False)

# Modelo de Produto
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), index=True, nullable=False)
    foto = Column(BLOB, nullable=True)  # Armazena imagens no banco
