class ErroTokenInvalido(Exception):
    def __init__(self):
        super().__init__("O token não é valido para o uso!")
        
class ErroChaveInvalido(Exception):
    def __init__(self):
        super().__init__("A chave não é valida para o uso!")

class ErroEmailEOuSenhaIncorretos(Exception):
    def __init__(self):
        super().__init__("O email e/ou a senha estao incorretos")

class ErroEmailJaCadastrado(Exception):
    def __init__(self):
        super().__init__("O email ja foi cadastrado")
