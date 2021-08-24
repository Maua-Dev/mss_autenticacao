class ErroCarregarEnv(Exception):
    def __init__(self):
        super().__init__("Nao foi possivel carregar o arquivo .env")
        
class ErroAssinaturaExpirada(Exception):
    def __init__(self):
        super().__init__("O tempo de sua assinatura acabou.")
        
class ErroFalhaDecoder(Exception):
    def __init__(self):
        super().__init__("O decoder falhou em decodificar.")
        
class ErroValidacao(Exception):
    def __init__(self):
        super().__init__("A assinatura passada não bate.") #TODO.: ADD A WAY TO ALERT THE SYSTEM IF SOMEONE IS DOING IT?