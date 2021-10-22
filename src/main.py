from fastapi import FastAPI, Request

from src.fabricas.controladores.fastapi.fabrica_controlador_fastapi import FabricaControladorFastAPI
from src.repositorios.jwt.authJWT import AuthJWT

from src.repositorios.volatil.armazenamento_volatil import ArmazenamentoUsuarioVolatil
from src.controladores.hashing.bcrypt.c_operacoes_bcrypt import COperacoesBcrypt


app = FastAPI()

armazenamento = ArmazenamentoUsuarioVolatil()
auth = AuthJWT()

factory = FabricaControladorFastAPI(auth, armazenamento, COperacoesBcrypt)

@app.get("/")
async def root():
    return {"mss": "autenticacao",
            "porta": 8080}

@app.post("/login")
async def logar(request: Request):
    return factory.logar(await request.json())

@app.post("/cadastrar")
async def cadastrarLogin(request: Request):
    return factory.cadastrarLogin(await request.json())

@app.post("/atualiza/roles")
async def atualizarRoles(request: Request):
    return factory.atualizarRoles(await request.json())


