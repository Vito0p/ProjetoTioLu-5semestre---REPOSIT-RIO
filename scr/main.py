from fastapi import FastAPI
from settings.settings import HOST, PORT, RELOAD
import uvicorn

# Import das rotas/endpoints
from scr.app.funcionario_dao import router as funcionario_router
from scr.app.cliente_dao import router as cliente_router
from scr.app.produto_dao import router as produto_router

app = FastAPI()

# Mapeamento das rotas
app.include_router(funcionario_router)
app.include_router(cliente_router)
app.include_router(produto_router)

if __name__ == "__main__":
    uvicorn.run("scr.main:app", host=HOST, port=int(PORT), reload=RELOAD)
