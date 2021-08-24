from src.controladores import fabrica
from fastapi import FastAPI, Request

from src.controladores.fabrica.fabrica_controlador_fastapi import FabricaControladorFastAPI
from src.repositorios.jwt.authJWT import AuthJWT
from src.repositorios.oauth.authOAuth import AuthOAuth
from src.repositorios.otp import authOTP

app = FastAPI()

controlador = FabricaControladorFastAPI(AuthJWT())

@app.get("/")
async def root():
    return {"mss": "autenticacao",
            "porta": 8080}

@app.post("/token")
async def gerarToken(request: Request):
    return controlador.gerarToken(await request.json())

@app.post("/verificar")
async def verificarToken(request: Request):
    return controlador.verificarToken(await request.body())
