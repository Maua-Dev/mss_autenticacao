from src.models.token import Token

from src.interfaces.i_auth import IAuth

from src.usecases.erros.erros_uc import ErroTokenInvalido

class UCCriarToken():

    auth : IAuth
    
    def __init__(self, auth : IAuth):
        self.auth = auth
        
    def __call__(self, token: Token):
        if self.auth.isTokenInvalido(token):
            raise ErroTokenInvalido
        return self.auth.criarToken(token)
