from src.models.token import Token

from src.interfaces.i_auth import IAuth


class UCTokenInvalido():

    auth : IAuth
    
    def __init__(self, auth : IAuth):
        self.auth = auth
        
    def __call__(self, token: Token):
        return self.auth.tokenInvalido(token)
