from fastapi import Response
from src.models import token

from src.models.token import Token

from src.interfaces.i_auth import IAuth
from src.interfaces.i_armazenamento_auth import IArmazenamento

from src.usecases.uc_esqueci_senha import UCEsqueciSenha
from src.usecases.uc_criar_token import UCCriarToken

from fastapi import Response

from http import HTTPStatus

class CEsqueciSenhaFastAPI():
    
    auth : IAuth
    
    def __init__(self, repo:IArmazenamento, auth: IAuth):
        self.repo = repo
        self.auth = auth
        
    def __call__(self, body: dict):
        try:

            if (self.repo.emailExiste(body["email"])):
                token = Token.fromDict(self._criarPayload(body["email"]))
                content = UCCriarToken(self.auth)(token)
                response = Response(content=str(content), status_code=HTTPStatus.ACCEPTED)
            else:
                response = Response(content="Email não encontrado ou não existe.", status_code=400)
        except:
            response = Response(content="Error", status_code=400)
            
        return response

    def _criarPayload(self, email: str):
        return {"payload": {"email": str(email)}}