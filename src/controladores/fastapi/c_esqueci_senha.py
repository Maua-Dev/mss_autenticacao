from fastapi import Response
from src.models import token

from src.models.token import Token

from src.interfaces.i_auth import IAuth
from src.interfaces.i_armazenamento_auth import IArmazenamento

from src.usecases.uc_esqueci_senha import UCEsqueciSenha
from src.usecases.uc_criar_token import UCCriarToken

from src.models.erros.erros_models import  ErroEmailInvalido, ErroEmailVazio

from fastapi import Response, status
from src.controladores.fastapi.http.requisicoes import ModeloEsqueciSenha


class CEsqueciSenhaFastAPI():
    
    auth : IAuth
    
    def __init__(self, repo:IArmazenamento, auth: IAuth):
        self.repo = repo
        self.auth = auth
        
    def __call__(self, esqueciSenha: ModeloEsqueciSenha):
        try:
            content = UCEsqueciSenha(self.repo, self.auth)(esqueciSenha.email)
            response = Response(content=content, status_code=status.HTTP_200_OK)
        except ErroEmailInvalido:
            response = Response(content="Esse email não existe", status_code=status.HTTP_404_NOT_FOUND)
        except ErroEmailVazio:
            response = Response(content="Recebido valor vazio. Favor digite um email.", status_code=status.HTTP_404_NOT_FOUND)
        except:
            response = Response(content="error undefined", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        return response