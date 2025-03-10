from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from scr.domain.entities.models import Funcionario, Cliente, Produto

# 🚀 FUNÇÕES CRUD PARA FUNCIONÁRIOS

# Buscar funcionário por CPF
async def get_funcionario_by_cpf(db: AsyncSession, cpf: str):
    result = await db.execute(select(Funcionario).filter(Funcionario.cpf == cpf))
    return result.scalars().first()

# Criar um novo funcionário
async def create_funcionario(db: AsyncSession, funcionario: Funcionario):
    db.add(funcionario)
    await db.commit()
    await db.refresh(funcionario)
    return funcionario

# Atualizar funcionário
async def update_funcionario(db: AsyncSession, funcionario: Funcionario):
    await db.commit()
    return funcionario

# Deletar funcionário
async def delete_funcionario(db: AsyncSession, funcionario: Funcionario):
    await db.delete(funcionario)
    await db.commit()

# Buscar todos os funcionários
async def get_all_funcionarios(db: AsyncSession):
    result = await db.execute(select(Funcionario))
    return result.scalars().all()


# 🚀 FUNÇÕES CRUD PARA CLIENTES

# Buscar cliente por CPF
async def get_cliente_by_cpf(db: AsyncSession, cpf: str):
    result = await db.execute(select(Cliente).filter(Cliente.cpf == cpf))
    return result.scalars().first()

# Criar um novo cliente
async def create_cliente(db: AsyncSession, cliente: Cliente):
    db.add(cliente)
    await db.commit()
    await db.refresh(cliente)
    return cliente

# Buscar todos os clientes
async def get_all_clientes(db: AsyncSession):
    result = await db.execute(select(Cliente))
    return result.scalars().all()

# Atualizar cliente
async def update_cliente(db: AsyncSession, cliente: Cliente):
    await db.commit()
    return cliente

# Deletar cliente
async def delete_cliente(db: AsyncSession, cliente: Cliente):
    await db.delete(cliente)
    await db.commit()


# 🚀 FUNÇÕES CRUD PARA PRODUTOS

# Buscar todos os produtos
async def get_all_produtos(db: AsyncSession):
    result = await db.execute(select(Produto))
    return result.scalars().all()

# Criar um novo produto
async def create_produto(db: AsyncSession, produto: Produto):
    db.add(produto)
    await db.commit()
    await db.refresh(produto)
    return produto

# Atualizar produto
async def update_produto(db: AsyncSession, produto: Produto):
    await db.commit()
    return produto

# Deletar produto
async def delete_produto(db: AsyncSession, produto: Produto):
    await db.delete(produto)
    await db.commit()
