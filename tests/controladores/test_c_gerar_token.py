from src.models.m_jwt_token import JWTToken
from src.usecases.uc_criar_jwt import UCCriarJWT
from src.interfaces.i_jwt_encriptografar import IJWTEncriptografar
from fastapi import Response, responses

import pytest

class CHTTPGerarToken():
    
    def gerarToken(self, body: dict):
        
        try:
            modelJWTToken = JWTToken.criarJWTTokenPorDictionary(body)
            content = UCCriarJWT(IJWTEncriptografar).criarJWT(modelJWTToken=modelJWTToken)
            response = content
            
        except:
            response = Response(content="Error", status_code=400)

        return response

@pytest.mark.xfail
def testErrorController():
    controller = CHTTPGerarToken()
    dictionary = {
        "payload" : {"sub": "1234567890","name": "John Doe","iat": 1516239022},
        "chave" : "your-256-bit-secret",
        "algoritmo" : "HS256",
        "header" : {"typ": "JWT"}
    }
    response = controller.gerarToken(body=dictionary)
    jwtToken = JWTToken.criarJWTTokenPorDictionary(dictionary)
    content = UCCriarJWT(IJWTEncriptografar).criarJWT(modelJWTToken=jwtToken)
    
    assert (response == content)
    
