from fastapi import FastAPI, Request

from src.controladores.fabrica.fabrica_controlador_fastapi import FabricaControladorFastAPI
from src.repositorios.jwt.authJWT import AuthJWT

from src.controladores.fastapi.c_logar_fastapi import CLogarFastApi
from src.repositorios.volatil.armazenamento_volatil import ArmazenamentoUsuarioVolatil
from src.controladores.fastapi.c_cadastrar_login_auth_fastapi import CCadastrarLoginAuthFastApi
from src.controladores.fastapi.c_atualizar_roles import CAtualizarRolesFastApi
from src.controladores.hashing.bcrypt.c_operacoes_bcrypt import COperacoesBcrypt


app = FastAPI()

armazenamento = ArmazenamentoUsuarioVolatil()
auth = AuthJWT()

controllerHash = COperacoesBcrypt
controllerLogin = CLogarFastApi(armazenamento, auth, COperacoesBcrypt)
controllerCadastrarLoginAuth = CCadastrarLoginAuthFastApi(armazenamento, COperacoesBcrypt)
controllerAtualizarRoles = CAtualizarRolesFastApi(armazenamento)

controladorJwt = FabricaControladorFastAPI(auth)

@app.get("/")
async def root():
    return {"mss": "autenticacao",
            "porta": 8080}

@app.post("/login")
async def logar(request: Request):
    return controllerLogin(await request.json())

@app.post("/cadastrar")
async def cadastrarLogin(request: Request):
    return controllerCadastrarLoginAuth(await request.json())

@app.post("/atualiza/roles")
async def atualizarRoles(request: Request):
    return controllerAtualizarRoles(await request.json())

@app.post("/verificar")
async def verificarToken(request: Request):
    return controladorJwt.verificarToken(await request.body())

