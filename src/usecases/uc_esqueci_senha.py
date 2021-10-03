from src.repositorios.erros.erros_volatil import ErroEmailNaoEncontrado
from src.interfaces.i_armazenamento_auth import IArmazenamento

class UCEsqueciSenha():

    auth : IArmazenamento
    
    def __init__(self, auth : IArmazenamento):
        self.auth = auth
        
    def __call__(self, email: str):
        if self.auth.emailExiste(email):
            raise ErroEmailNaoEncontrado
        return self.auth.esqueciSenha(email)
