from fastapi import Response, status
from pydantic.errors import EmailError
from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login
from src.repositorios.erros.erros_volatil import ErroEmailNaoEncontrado
from src.usecases.uc_usuario_auth import UCUsuarioAuth
from src.interfaces.i_auth import IAuth
from src.interfaces.i_operacoes_hash import IOperacoesHash

from src.controladores.fastapi.http.requisicoes import AlterarSenha


class CAlterarSenhaFastApi():
    repo: IArmazenamento
    uc: UCUsuarioAuth
    auth: IAuth
    
    def __init__(self, repo: IArmazenamento, auth: IAuth, iHash: IOperacoesHash):
        self.repo = repo
        self.auth = auth
        self.iHash = iHash
        self.uc = UCUsuarioAuth(self.repo, iHash)
        
    def __call__(self, alterarSenha: AlterarSenha):
        
        try:
            token = self.auth.verificarToken(alterarSenha.token)
            if alterarSenha.email == token["email"]:
                login = Login.fromDict({"email":alterarSenha.email, "senha":alterarSenha.novasenha})
                self.uc.alterarSenha(login)
                return Response(content="Senha atualizada com successo", status_code=status.HTTP_202_ACCEPTED)
            else:
                return Response(content="Email não bate", status_code=status.HTTP_400_BAD_REQUEST)
            
        except ErroEmailNaoEncontrado:
            return Response(content="Erro - Email não encontrado", status_code=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response(content="Erro inesperado", status_code=status.HTTP_404_NOT_FOUND)