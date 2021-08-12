from src.interfaces.i_geracao import IGeracao


class UCCarregarChave():

    geracao : IGeracao
    
    def __init__(self, geracao : IGeracao):
        self.geracao = geracao
        
    def __call__(self):
        return self.geracao.carregarChave()
