from http import HTTPStatus
from fastapi import responses
from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login
from src.repositorios.erros.erros_volatil import ErroEmailNaoEncontrado
from src.usecases.uc_usuario_auth import UCUsuarioAuth
from src.interfaces.i_auth import IAuth
from src.interfaces.i_operacoes_hash import IOperacoesHash


class CAlterarSenhaFastApi():
    repo: IArmazenamento
    uc: UCUsuarioAuth
    auth: IAuth
    
    def __init__(self, repo: IArmazenamento, auth: IAuth, iHash: IOperacoesHash):
        self.repo = repo
        self.auth = auth
        self.iHash = iHash
        self.uc = UCUsuarioAuth(self.repo, iHash)
        
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
            if body["email"] == token["email"]:
                login = Login.fromDict({"email":body["email"], "senha":body["novasenha"]})
                self.uc.alterarSenha(login)
                return responses(content="Senha atualizada com successo", status_code=HTTPStatus.ACCEPTED)
            else:
                return responses(content="Email não encontrado", status_code=HTTPStatus.BAD_REQUEST)
        except ErroEmailNaoEncontrado:
            return responses(content="Erro - Email não encontrado", status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
        except Exception:
            return responses(content="Erro inesperado", status_code=HTTPStatus.INTERNAL_SERVER_ERROR)