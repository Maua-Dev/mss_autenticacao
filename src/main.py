from fastapi import FastAPI, Request

from src.controladores.c_gerar_token_fastapi import CGerarTokenFastAPI
from src.repositorios.jwt.authJWT import AuthJWT
from src.repositorios.oauth.authOAuth import AuthOAuth
from src.repositorios.otp import authOTP

from src.usecases.uc_criar_token import UCCriarToken

app = FastAPI()

controllerGerarToken = CGerarTokenFastAPI(AuthJWT())

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/token")
async def gerarToken(request: Request):
    return controllerGerarToken(await request.json())