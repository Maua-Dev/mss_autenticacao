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

class ErroEmailVazio(Exception):
    def __init__(self):
        super().__init__("Email está vazio")

class ErroEmailInvalido(Exception): # Estrutura mail@mail.com
    def __init__(self):
        super().__init__("Email invalido")

class ErroConversaoRequestLogin(Exception):
    def __init__(self):
        super().__init__("Nao foi possivel converter a requisicao para um login")

class ErroConversaoStrRole(Exception):
    def __init__(self):
        super().__init__("Nao foi possivel converter a lista de str para roles")

