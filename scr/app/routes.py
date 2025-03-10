from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from scr.infra.database import get_db
from scr.app.crud import (
    get_funcionario_by_cpf, create_funcionario, update_funcionario, delete_funcionario, get_all_funcionarios,
    get_cliente_by_cpf, create_cliente, update_cliente, delete_cliente, get_all_clientes,
    create_produto, update_produto, delete_produto, get_all_produtos
)
from scr.domain.schemas import FuncionarioSchema, ClienteSchema, ProdutoSchema
from scr.domain.entities.models import Funcionario, Cliente, Produto

router = APIRouter()

# 🚀 ROTA PARA FUNCIONÁRIOS

@router.post("/funcionario/")
async def create_funcionario_route(funcionario: FuncionarioSchema, db: AsyncSession = Depends(get_db)):
    db_funcionario = await get_funcionario_by_cpf(db, funcionario.cpf)
    if db_funcionario:
        raise HTTPException(status_code=400, detail="CPF já cadastrado")

    novo_funcionario = Funcionario(nome=funcionario.nome, cpf=funcionario.cpf, senha=funcionario.senha)
    return await create_funcionario(db, novo_funcionario)

@router.get("/funcionario/")
async def list_funcionarios_route(db: AsyncSession = Depends(get_db)):
    return await get_all_funcionarios(db)

@router.put("/funcionario/{cpf}")
async def update_funcionario_route(cpf: str, funcionario: FuncionarioSchema, db: AsyncSession = Depends(get_db)):
    db_funcionario = await get_funcionario_by_cpf(db, cpf)
    if not db_funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")

    db_funcionario.nome = funcionario.nome
    db_funcionario.senha = funcionario.senha
    return await update_funcionario(db, db_funcionario)

@router.delete("/funcionario/{cpf}")
async def delete_funcionario_route(cpf: str, db: AsyncSession = Depends(get_db)):
    db_funcionario = await get_funcionario_by_cpf(db, cpf)
    if not db_funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")

    await delete_funcionario(db, db_funcionario)
    return {"msg": "Funcionário deletado com sucesso"}


# 🚀 ROTA PARA CLIENTES

@router.post("/cliente/")
async def create_cliente_route(cliente: ClienteSchema, db: AsyncSession = Depends(get_db)):
    db_cliente = await get_cliente_by_cpf(db, cliente.cpf)
    if db_cliente:
        raise HTTPException(status_code=400, detail="CPF já cadastrado")

    novo_cliente = Cliente(nome=cliente.nome, cpf=cliente.cpf)
    return await create_cliente(db, novo_cliente)

@router.get("/cliente/")
async def list_clientes_route(db: AsyncSession = Depends(get_db)):
    return await get_all_clientes(db)

@router.put("/cliente/{cpf}")
async def update_cliente_route(cpf: str, cliente: ClienteSchema, db: AsyncSession = Depends(get_db)):
    db_cliente = await get_cliente_by_cpf(db, cpf)
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    db_cliente.nome = cliente.nome
    return await update_cliente(db, db_cliente)

@router.delete("/cliente/{cpf}")
async def delete_cliente_route(cpf: str, db: AsyncSession = Depends(get_db)):
    db_cliente = await get_cliente_by_cpf(db, cpf)
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    await delete_cliente(db, db_cliente)
    return {"msg": "Cliente deletado com sucesso"}


# 🚀 ROTA PARA PRODUTOS

@router.post("/produto/")
async def create_produto_route(produto: ProdutoSchema, db: AsyncSession = Depends(get_db)):
    novo_produto = Produto(nome=produto.nome, foto=produto.foto)
    return await create_produto(db, novo_produto)

@router.get("/produto/")
async def list_produtos_route(db: AsyncSession = Depends(get_db)):
    return await get_all_produtos(db)

@router.put("/produto/{id}")
async def update_produto_route(id: int, produto: ProdutoSchema, db: AsyncSession = Depends(get_db)):
    produtos = await get_all_produtos(db)
    db_produto = next((p for p in produtos if p.id == id), None)
    
    if not db_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    db_produto.nome = produto.nome
    db_produto.foto = produto.foto
    return await update_produto(db, db_produto)

@router.delete("/produto/{id}")
async def delete_produto_route(id: int, db: AsyncSession = Depends(get_db)):
    produtos = await get_all_produtos(db)
    db_produto = next((p for p in produtos if p.id == id), None)

    if not db_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    await delete_produto(db, db_produto)
    return {"msg": "Produto deletado com sucesso"}
