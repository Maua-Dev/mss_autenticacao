from src.models.token import Token

from src.interfaces.i_geracao import IGeracao


class UCTokenInvalido():

    geracao : IGeracao
    
    def __init__(self, geracao : IGeracao):
        self.geracao = geracao
        
    def __call__(self, token: Token):
        return self.geracao.tokenInvalido(token)
