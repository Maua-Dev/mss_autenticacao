class ErroFalhaConectar(Exception):
    def __init__(self):
        super().__init__("Falha em realizar a conexao")

class ErroCriar(Exception):
    def __init__(self):
        super().__init__("Error ao tentar criar indice")

class ErroEditar(Exception):
    def __init__(self):
        super().__init__("Error ao tentar editar indice")

class ErroLer(Exception):
    def __init__(self):
        super().__init__("Error ao tentar ler indice")

class ErroDeletar(Exception):
    def __init__(self):
        super().__init__("Error ao tentar deletar indice")