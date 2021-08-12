from fastapi import Response

from src.models.chave import Chave
from src.models.token import Token

from src.interfaces.i_geracao import IGeracao

from src.usecases.uc_criar_token import UCCriarToken

from fastapi import Response, responses

class CHTTPGerarToken():
    
    def gerarToken(self, body: dict, criarTokenUC : UCCriarToken):
        try:
            token = Token.fromDict(body)
            content = criarTokenUC(token)
            response = Response(content=str(content), status_code=200)
            
        except:
            response = Response(content="Error", status_code=400)

        return response
    