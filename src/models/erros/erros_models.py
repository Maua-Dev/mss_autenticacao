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
        super().__init__("Email inválido")


# Esse erro não deve ser passado para o usuário final
class ErroConversaoRequestLogin(Exception):
    def __init__(self):
        super().__init__("Não foi possível converter a requisição para um login")

# Esse erro não deve ser passado para o usuário final
class ErroConversaoStrRole(Exception):
    def __init__(self):
        super().__init__("Não foi possível converter a lista de roles para Roles")

