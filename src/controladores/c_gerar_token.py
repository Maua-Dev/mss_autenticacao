from src.models.m_jwt_chave import JWTChave
from src.models.m_jwt_token import JWTToken

from src.interfaces.i_jwt_encriptografar import IJWTEncriptografar

from src.usecases.uc_criar_chave import UCCriarChave
from src.usecases.uc_criar_jwt import UCCriarJWT

from fastapi import Response, responses

class CHTTPGerarToken():
    
    def gerarToken(self, body: dict):
        
        try:
            modelJWTToken = JWTToken.criarJWTTokenPorDictionary(body)
            content = UCCriarJWT(IJWTEncriptografar).criarJWT(modelJWTToken=modelJWTToken, chave="tempkey")
            response = Response(content=str(content), status_code=200)
            
        except:
            response = Response(content="Error", status_code=400)

        return response
    