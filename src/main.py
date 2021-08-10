from fastapi import FastAPI
from starlette.requests import Request

from src.controladores.c_gerar_token import CHTTPGerarToken

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/token")
async def gerarToken(request: Request):
    result = await request.json()
    return CHTTPGerarToken().gerarToken(result)