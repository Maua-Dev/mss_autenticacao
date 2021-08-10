from fastapi import Response, responses

from src.usecases.uc_criar_jwt import UCCriarJWT
from src.usecases.uc_criar_chave import UCCriarChave

from src.models.m_jwt_chave import JWTChave
from src.models.m_jwt_token import JWTToken

class UCGerarJWT():

    def gerarJWT(self):

        try:
            
            #modelChave = ModelJWTChave()
            modelToken = JWTToken()
            
        except:
            response = Exception

        return response