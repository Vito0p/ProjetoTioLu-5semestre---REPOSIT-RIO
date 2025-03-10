import asyncio
from scr.infra.database import engine, Base
from scr.domain.entities.models import Funcionario, Cliente, Produto  # Importar os modelos

# Criar as tabelas no banco de dados
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Executar a criação das tabelas
if __name__ == "__main__":
    asyncio.run(init_db())
