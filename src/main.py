from fastapi import FastAPI, Request

from src.controladores.fabrica.fabrica_controlador_fastapi import FabricaControladorFastAPI
from src.repositorios.jwt.authJWT import AuthJWT

from src.controladores.fastapi.c_logar_fastapi import CLogarFastApi
from src.repositorios.volatil.armazenamento_volatil import ArmazenamentoUsuarioVolatil
from src.controladores.fastapi.c_cadastrar_login_auth_fastapi import CCadastrarLoginAuthFastApi
from src.controladores.fastapi.c_atualizar_roles import CAtualizarRolesFastApi
from src.controladores.hashing.bcrypt.c_operacoes_bcrypt import COperacoesBcrypt
from src.controladores.fastapi.http.requisicoes import EsqueciSenha, AlterarSenha


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

@app.post("/esquecisenha")
async def esqueciSenha(esqueciSenha: EsqueciSenha):
    return factory.esqueciSenha(esqueciSenha.email)

@app.post("/alterarsenha")
async def esqueciSenha(alterarSenha: AlterarSenha):
    return factory.alterarSenha(alterarSenha)


