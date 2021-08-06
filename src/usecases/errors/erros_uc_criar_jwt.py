class ErroPayloadInvalido(Exception):
    def __init__(self):
        super().__init__("Payload invalido")
        
class ErroSecretInvalido(Exception):
    def __init__(self):
        super().__init__("Secret invalido")

class ErroAlgoritmoInvalido(Exception):
    def __init__(self):
        super().__init__("Algoritmo invalido")
        
class ErroPayloadVazio(Exception):
    def __init__(self):
        super().__init__("Nao ha Payload")
        
class ErroSecretVazio(Exception):
    def __init__(self):
        super().__init__("Nao ha Secret")

class ErroAlgoritmoVazio(Exception):
    def __init__(self):
        super().__init__("Nao ha Algoritmo")
        
class ErroFalhaCriar(Exception):
    def __init__(self):
        super().__init__("Falha em criar o Token.")