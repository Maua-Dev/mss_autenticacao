class ErroHeaderVazio(Exception):
    def __init__(self):
        super().__init__("Header enviado está vazio!")
        
class ErroPayloadVazio(Exception):
    def __init__(self):
        super().__init__("Payload enviado está vazio!")
        
class ErroChaveVazio(Exception):
    def __init__(self):
        super().__init__("Chave enviada está vazia!")
        
class ErroAlgoritmoVazio(Exception):
    def __init__(self):
        super().__init__("Algoritmo enviado está vazio!")
        
class ErroSenhaVazio(Exception):
    def __init__(self):
        super().__init__("Senha enviada está vazia!")
        
class ErroSenhaVazio(Exception):
    def __init__(self):
        super().__init__("Senha enviada está vazia!")