from src.models.chave import Chave

from src.interfaces.i_geracao import IGeracao

from src.usecases.errors.erros_uc import ErroChaveInvalido


class UCCriarChave():

    geracao : IGeracao
    
    def __init__(self, geracao : IGeracao):
        self.geracao = geracao
        
    def __call__(self, chave: Chave):
        if self.geracao.senhaInvalido(chave):
            raise ErroChaveInvalido
        return self.geracao.criarChave(chave)