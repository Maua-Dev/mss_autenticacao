class ErroTokenInvalido(Exception):
    def __init__(self):
        super().__init__("O token não é valido para o uso!")
        
class ErroChaveInvalido(Exception):
    def __init__(self):
        super().__init__("A chave não é valida para o uso!")