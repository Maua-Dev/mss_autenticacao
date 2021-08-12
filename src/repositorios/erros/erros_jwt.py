class ErroCarregarEnv(Exception):
    def __init__(self):
        super().__init__("Nao foi possivel carregar o arquivo .env")