from fastapi import FastAPI, Request

from src.controladores.c_gerar_token_fastapi import CGerarTokenFastAPI
from src.repositorios.jwt.authJWT import AuthJWT
from src.repositorios.oauth.authOAuth import AuthOAuth
from src.repositorios.otp import authOTP
from src.controladores.c_logar_fastapi import CLogarFastApi
from src.repositorios.volatil.armazenamento_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.uc_criar_token import UCCriarToken
from src.controladores.c_cadastrar_login_auth_fastapi import CCadastrarLoginAuthFastApi


app = FastAPI()

armazenamento = ArmazenamentoUsuarioVolatil()
auth = AuthJWT()

controllerGerarToken = CGerarTokenFastAPI(auth)
# controllerLogin = CLogarFastApi(armazenamento, auth)
controllerLogin = CLogarFastApi(armazenamento)
controllerCadastrarLoginAuth = CCadastrarLoginAuthFastApi(armazenamento)

@app.get("/")
async def root():
    return {"mss": "autenticacao",
            "porta": 8080}

@app.post("/token")
async def gerarToken(request: Request):
    return controllerGerarToken(await request.json())

@app.post("/login")
async def logar(request: Request):
    return controllerLogin(await request.json())

@app.post("/cadastrar")
async def cadastrarLogin(request: Request):
    return controllerCadastrarLoginAuth(await request.json())
