from src.usecases.uc_login import UCLogin
from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login
from fastapi import Response
from src.usecases.uc_usuario_auth import UCUsuarioAuth
from src.usecases.uc_criar_token import UCCriarToken
from src.interfaces.i_auth import IAuth
from http import HTTPStatus
from src.models.erros.erros_models import ErroEmailVazio, ErroEmailInvalido, ErroSenhaVazio, ErroConversaoRequestLogin, ErroConversaoStrRole
from src.usecases.errors.erros_uc import ErroEmailEOuSenhaIncorretos
from src.repositorios.erros.erros_volatil import ErroEmailNaoEncontrado
from src.models.token import Token


class CLogarFastApi():
    repo: IArmazenamento
    ucLogin: UCLogin
    ucRepo: UCUsuarioAuth
    auth: IAuth

    def __init__(self, repo: IArmazenamento, auth: IAuth):
        self.repo = repo
        self.ucLogin = UCLogin(self.repo)
        self.ucRepo = UCUsuarioAuth(self.repo)
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

            if self.ucLogin.autenticaLogin(login):
                content = UCCriarToken(self.auth)(Token.fromDict(self._criarPayload(login.email)))
                print(content)

            #TODO Considerar trocar Response para um model response que tenha mensagem e codigo -> Paramos de depender do FastApi
            return Response(content=content, status_code=HTTPStatus.OK)

        except (ErroEmailVazio, ErroEmailInvalido, ErroSenhaVazio, ErroConversaoRequestLogin, ErroConversaoStrRole) as e:
            return Response(content=str(e), status_code=HTTPStatus.BAD_REQUEST)

        except ErroEmailEOuSenhaIncorretos as e:
            return Response(content=str(e), status_code=HTTPStatus.UNAUTHORIZED)

        except ErroEmailNaoEncontrado as e:  # Levantado por chamada ucRepo.getRolesPorEmail()
            return Response(content=str(e), status_code=HTTPStatus.NOT_FOUND)

        except Exception:
            return Response(content="Erro inesperado", status_code=HTTPStatus.INTERNAL_SERVER_ERROR)

    def _criarPayload(self, email: str):
        return {"payload": {"email": str(email), "roles": self.ucRepo.getRolesPorEmail(email)}}
