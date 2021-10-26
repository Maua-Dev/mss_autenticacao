from src.usecases.uc_login import UCLogin
from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login
from fastapi import Response, status
from src.usecases.uc_usuario_auth import UCUsuarioAuth
from src.usecases.uc_criar_token import UCCriarToken
from src.interfaces.i_auth import IAuth
from src.models.erros.erros_models import ErroEmailVazio, ErroEmailInvalido, ErroSenhaVazio, ErroConversaoRequestLogin, ErroConversaoStrRole
from src.usecases.erros.erros_uc import ErroEmailEOuSenhaIncorretos, ErroInesperado
from src.repositorios.erros.erros_volatil import ErroEmailNaoEncontrado
from src.models.token import Token
from src.interfaces.i_operacoes_hash import IOperacoesHash
import logging


class CLogarFastApi:
    repo: IArmazenamento
    ucLogin: UCLogin
    ucRepo: UCUsuarioAuth
    auth: IAuth

    def __init__(self, repo: IArmazenamento, auth: IAuth, iHash: IOperacoesHash):
        self.repo = repo
        self.ucLogin = UCLogin(self.repo, iHash)
        self.ucRepo = UCUsuarioAuth(self.repo, iHash)
        self.auth = auth

    # def __init__(self, repo: IArmazenamento):
    #     self.repo = repo
    #     self.ucLogin = UCLogin(self.repo)
    #     self.ucRepo = UCUsuarioAuth(self.repo)

    def __call__(self, body: dict):

        """
        Estrutura do body:
        {
            'email': email
            'senha': senha
        }
        """
        try:
            login = Login.fromDict(body)

            if self.ucLogin.autenticarLogin(login):
                content = UCCriarToken(self.auth)(Token.fromDict(self._criarPayload(login.email)))
            # Considerar levantar false ao inves de erro --> (talvez NAO faz sentido ter if aqui do jeito que esta agr - redundante)
            return Response(content=content, status_code=status.HTTP_200_OK)

        except (ErroEmailVazio, ErroEmailInvalido, ErroSenhaVazio, ErroConversaoRequestLogin, ErroConversaoStrRole) as e:
            return Response(content=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except ErroEmailEOuSenhaIncorretos as e:
            return Response(content=str(e), status_code=status.HTTP_401_UNAUTHORIZED)

        except ErroEmailNaoEncontrado as e:  # Levantado por chamada ucRepo.getRolesPorEmail()
            return Response(content=str(e), status_code=status.HTTP_404_NOT_FOUND)

        except Exception:
            logging.exception(str(ErroInesperado()))
            return Response(content=str(ErroInesperado()), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def _criarPayload(self, email: str):
        return {"payload": {"email": str(email), "roles": self.ucRepo.getRolesPorEmail(email)}}
