from fastapi import Response, responses

from src.usecases.uc_criar_jwt import UseCaseCriarJWT
from src.usecases.uc_criar_chave import UseCaseCriarChave

from src.models.m_jwt_chave import ModelJWTChave
from src.models.m_jwt_token import ModelJWTToken

class ControllerHTTPGerarJWT():

    def gerarJWT(self):

        try:
            
            #modelChave = ModelJWTChave()
            modelToken = ModelJWTToken()
            
        except:
            response = Exception

        return response