from src.models.chave import Chave

from src.interfaces.i_auth import IAuth

from src.usecases.errors.erros_uc import ErroChaveInvalido


class UCCriarChave():

    auth : IAuth
    
    def __init__(self, auth : IAuth):
        self.auth = auth
        
    def __call__(self, chave: Chave):
        if self.auth.senhaInvalido(chave):
            raise ErroChaveInvalido
        return self.auth.criarChave(chave)