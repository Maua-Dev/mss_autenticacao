from src.models.token import Token
from src.models.login import Login
from src.repositorios.erros.erros_volatil import ErroEmailNaoEncontrado
from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.interfaces.i_auth import IAuth

class UCRecuperarSenha():

    auth : IArmazenamento
    
    def __init__(self, repo: IArmazenamento, auth: IAuth):
        self.repo = repo
        self.auth = auth
        
    def __call__(self, response: str, email: str, novasenha: str):
        try:
            token = self.auth.verificarToken(response)
            if email == token["payload"]["email"]:
                self.repo.alterarSenha()
            pass
        except:
            pass
        