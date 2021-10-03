from fastapi import Response
from src.models import token

from src.models.token import Token

from src.interfaces.i_auth import IAuth
from src.interfaces.i_armazenamento_auth import IArmazenamento

from src.usecases.uc_esqueci_senha import UCEsqueciSenha
from src.usecases.uc_criar_token import UCCriarToken

from src.models.erros.erros_models import  ErroEmailInvalido, ErroEmailVazio

from fastapi import Response

from http import HTTPStatus

class CEsqueciSenhaFastAPI():
    
    auth : IAuth
    
    def __init__(self, repo:IArmazenamento, auth: IAuth):
        self.repo = repo
        self.auth = auth
        
    def __call__(self, body: dict):
        try:
            content = UCEsqueciSenha(self.repo, self.auth)(body["email"])
            response = Response(content=content, status_code=HTTPStatus.ACCEPTED)
        except ErroEmailInvalido:
            response = Response(content="Esse email não existe", status_code=400)
        except ErroEmailVazio:
            response = Response(content="Recebido valor vazio. Favor digite um email.", status_code=400)
        except:
            response = Response(content="error undefined", status_code=400)
            
        return response