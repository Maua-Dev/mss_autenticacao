from src.models.token import Token

from src.interfaces.i_geracao import IGeracao

from src.usecases.errors.erros_uc import ErroTokenInvalido

class UCCriarToken():

    geracao : IGeracao
    
    def __init__(self, geracao : IGeracao):
        self.geracao = geracao
        
    def __call__(self, token: Token):
        if self.geracao.tokenInvalido(token):
            raise ErroTokenInvalido
        return self.geracao.criarToken(token)
