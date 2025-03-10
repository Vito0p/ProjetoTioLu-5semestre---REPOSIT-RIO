from fastapi import FastAPI
from scr.app.routes import router
import uvicorn

app = FastAPI(title="Projeto CRUD FastAPI - Funcionário, Cliente e Produto")

# Registrar as rotas no FastAPI
app.include_router(router)

# Rodar a aplicação
if __name__ == "__main__":
    uvicorn.run("scr.main:app", host="127.0.0.1", port=8000, reload=True)
