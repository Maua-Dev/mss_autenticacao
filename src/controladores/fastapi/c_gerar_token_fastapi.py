from fastapi import Response
from src.models import token

from src.models.chave import Chave
from src.models.token import Token

from src.interfaces.i_auth import IAuth

from src.usecases.uc_criar_token import UCCriarToken

from fastapi import Response


class CGerarTokenFastAPI():
    
    auth: IAuth
    
    def __init__(self, auth: IAuth):
        self.auth = auth
        
    def __call__(self, body: dict):
        try:
            token = Token.fromDict(body)
            content = UCCriarToken(self.auth)(token)
            response = Response(content=str(content), status_code=200)
        except:
            response = Response(content="Error", status_code=400)
            
        return response
