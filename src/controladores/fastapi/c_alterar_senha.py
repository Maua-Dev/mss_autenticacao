from fastapi import Response, status
from pydantic.errors import EmailError
from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login
from src.repositorios.erros.erros_volatil import ErroEmailNaoEncontrado
from src.usecases.uc_usuario_auth import UCUsuarioAuth
from src.interfaces.i_auth import IAuth
from src.interfaces.i_operacoes_hash import IOperacoesHash
from src.repositorios.erros.erros_token import ErroAssinaturaExpirada, ErroFalhaDecoder, ErroValidacao

from src.controladores.fastapi.http.requisicoes import ModeloAlterarSenha


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
        
        try:
            token = self.auth.verificarToken(body["token"])
            if body["email"] == token["email"]:
                login = Login.fromDict({"email":body["email"], "senha":body["novasenha"]})
                self.uc.alterarSenha(login)
                return Response(content="Senha atualizada com successo", status_code=status.HTTP_200_OK)
            else:
                return Response(content="Email não bate", status_code=status.HTTP_404_NOT_FOUND)
            
        except ErroValidacao:
            return Response(content="Token inválido. Tentativa de acessar o sistema registrado.", status_code=status.HTTP_403_FORBIDDEN)
        except ErroAssinaturaExpirada:
            return Response(content="Token expirado.", status_code=status.HTTP_504_GATEWAY_TIMEOUT)
        except ErroEmailNaoEncontrado:
            return Response(content="Erro - Email não encontrado", status_code=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response(content="Erro inesperado", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)