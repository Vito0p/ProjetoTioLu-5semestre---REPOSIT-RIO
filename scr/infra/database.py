from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL do banco de dados SQLite (ele será salvo como um arquivo local)
DATABASE_URL = "sqlite+aiosqlite:///./database.db"

# Criar o motor do banco de dados
engine = create_async_engine(DATABASE_URL, echo=True)

# Criar uma sessão assíncrona
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Base para os modelos ORM
Base = declarative_base()

# Função para obter uma sessão do banco de dados
async def get_db():
    async with SessionLocal() as session:
        yield session
