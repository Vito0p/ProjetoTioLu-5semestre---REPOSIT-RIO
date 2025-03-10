from pydantic import BaseModel

# Schema para Funcionário
class FuncionarioSchema(BaseModel):
    nome: str
    cpf: str
    senha: str

# Schema para Cliente
class ClienteSchema(BaseModel):
    nome: str
    cpf: str

# Schema para Produto
class ProdutoSchema(BaseModel):
    nome: str
    foto: bytes | None  
