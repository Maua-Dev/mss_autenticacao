from src.models.login import Login
from src.repositorios.erros.erros_volatil import ErroEmailNaoEncontrado
from src.interfaces.i_armazenamento_auth import IArmazenamento

class UCRecuperarSenha():

    auth : IArmazenamento
    
    def __init__(self, auth : IArmazenamento):
        self.auth = auth
        
    def __call__(self, login: Login):
        return self.auth.alterarSenha(login)
