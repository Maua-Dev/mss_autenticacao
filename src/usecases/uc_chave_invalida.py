from src.models.chave import Chave

from src.interfaces.i_auth import IAuth


class UCChaveInvalida():

    auth : IAuth
    
    def __init__(self, auth : IAuth):
        self.auth = auth
        
    def __call__(self, chave: Chave):
        return self.auth.isChaveInvalida(chave)
