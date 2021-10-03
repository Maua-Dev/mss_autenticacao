from logging import raiseExceptions
from src.models.erros.erros_models import ErroEmailVazio, ErroEmailInvalido
from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.interfaces.i_auth import IAuth

from src.models.token import Token

class UCEsqueciSenha():

    auth : IArmazenamento
    
    def __init__(self, repo: IArmazenamento, auth: IAuth):
        self.repo = repo
        self.auth = auth
        
        
    def __call__(self, email: str):
        if not email:
            raise ErroEmailVazio
        if not self.repo.emailExiste(email):
            raise ErroEmailInvalido
        return self.auth.criarToken(Token.fromDict(self._criarPayload(email)))
        
    def _criarPayload(self, email: str):
        return {"payload": {"email": str(email)}}
