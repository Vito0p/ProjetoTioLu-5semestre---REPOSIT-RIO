from dotenv import load_dotenv, find_dotenv
import os

# Localiza e carrega as variáveis de ambiente do .env
dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

# Configurações da API
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
RELOAD = os.getenv("RELOAD")

# Garantindo que as variáveis não estão vazias
if not HOST or not PORT or not RELOAD:
    raise ValueError("Erro: Variáveis de ambiente não foram carregadas corretamente. Verifique o arquivo .env.")
