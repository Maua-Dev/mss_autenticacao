from src.models.chave import Chave

from src.interfaces.i_geracao import IGeracao


class UCChaveInvalido():

    geracao : IGeracao
    
    def __init__(self, geracao : IGeracao):
        self.geracao = geracao
        
    def __call__(self, chave: Chave):
        return self.geracao.chaveInvalido(chave)
