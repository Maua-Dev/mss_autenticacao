from fastapi import FastAPI, Request

from src.controladores.c_gerar_token import CHTTPGerarToken
from src.repositorios.criacao.jwt import JWTGeracao
from src.repositorios.criacao.oauth import OAuthGeracao
from src.repositorios.criacao.otp import OTPGeracao

from src.usecases.uc_criar_token import UCCriarToken

app = FastAPI()

geracaoJWT = JWTGeracao()
geracaoOAuth = OAuthGeracao()
geracaoOTP = OTPGeracao()

criarTokenUC = UCCriarToken(geracaoOTP)
criarTokenUC = UCCriarToken(geracaoOAuth)
criarTokenUC = UCCriarToken(geracaoJWT)

controllerGerarToken = CHTTPGerarToken()




@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/token")
async def gerarToken(request: Request):
    return controllerGerarToken.gerarToken(await request.json(), criarTokenUC)