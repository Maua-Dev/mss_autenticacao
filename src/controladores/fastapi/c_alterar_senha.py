from http import HTTPStatus
from fastapi import responses
from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login
from src.usecases.uc_usuario_auth import UCUsuarioAuth


class CAlterarSenhaFastApi():
    repo: IArmazenamento
    uc: UCUsuarioAuth
    
    def __init__(self, repo: IArmazenamento):
        self.repo = repo
        self.uc = UCUsuarioAuth(self.repo)
        
    def __call__(self, body: dict):
        """
        Estrutura do body:
        {
            'token': Token
            'email': str
            'novasenha' : str
        }
        """
        
        try:
            token = self.auth.verificarToken(body["token"])
            if body["email"] == token["payload"]["email"]:
                self.repo.alterarSenha(Login(body["email"], body["novasenha"]))
            else:
                return responses(content="Email não encontrado", status_code=HTTPStatus.BAD_REQUEST)
        except Exception:
            return responses(content="Erro inesperado", status_code=HTTPStatus.INTERNAL_SERVER_ERROR)