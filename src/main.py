from fastapi import FastAPI, Request

from src.controladores.c_gerar_token_fastapi import CGerarTokenFastAPI
from src.controladores.c_verificar_token import CVerificarToken
from src.repositorios.jwt.authJWT import AuthJWT
from src.repositorios.oauth.authOAuth import AuthOAuth
from src.repositorios.otp import authOTP

from src.usecases.uc_criar_token import UCCriarToken

app = FastAPI()

controllerGerarToken = CGerarTokenFastAPI(AuthJWT())
controllerVerificarToken = CVerificarToken(AuthJWT())

@app.get("/")
async def root():
    return {"mss": "autenticacao",
            "porta": 8080}

@app.post("/token")
async def gerarToken(request: Request):
    return controllerGerarToken(await request.json())

@app.post("/verificar")
async def verificarToken(request: Request):
    return controllerVerificarToken(await request.body())
