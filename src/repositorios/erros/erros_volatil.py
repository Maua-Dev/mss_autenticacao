
class ErroEmailNaoEncontrado(Exception):
    def __init__(self):
        super().__init__("O email nao foi encontrado")