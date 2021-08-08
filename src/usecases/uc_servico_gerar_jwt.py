from fastapi import Response, responses

from src.usecases.uc_criar_jwt import JWTToken
from src.usecases.uc_criar_chave import JWTChave

from src.models.m_jwt_chave import MJWTChave
from src.models.m_jwt_token import MJWTToken

class ControllerHTTPGerarJWT():

    def gerarJWT(self):

        try:
            
            #modelChave = MJWTChave()
            modelToken = MJWTToken()
            
        except:
            response = Exception

        return response