class ErroTokenInvalido(Exception):
    def __init__(self):
        super().__init__("O token não é válido para o uso!")
        
class ErroChaveInvalido(Exception):
    def __init__(self):
        super().__init__("A chave não é válida para o uso!")

class ErroEmailEOuSenhaIncorretos(Exception):
    def __init__(self):
        super().__init__("Email ou senha incorretos")

class ErroEmailJaCadastrado(Exception):
    def __init__(self):
        super().__init__("O email já foi cadastrado anteriormente")
