from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.usecases.uc_usuario_auth import UCUsuarioAuth
from fastapi import Response
from src.models.login import Login
from src.repositorios.erros.erros_volatil import ErroEmailNaoEncontrado
from http import HTTPStatus
from src.models.erros.erros_models import ErroEmailVazio, ErroEmailInvalido, ErroSenhaVazio, ErroConversaoRequestLogin, ErroConversaoStrRole


class CAtualizarRolesFastApi():
    repo: IArmazenamento
    uc: UCUsuarioAuth

    def __init__(self, repo: IArmazenamento):
        self.repo = repo
        self.uc = UCUsuarioAuth(self.repo)

    def __call__(self, body: dict):
        #TODO considerar passar list de int em vez de string
        """
        Estrutura do body:
        {
            'email': email
            'roles': [roles: str]
        }
        """
        try:
            roles = Login.rolesFromStrList(roles=body["roles"])
            self.uc.atualizaRoles(email=body["email"], roles=roles)

            return Response(content="atualizado com sucesso", status_code=200)

        except ErroEmailNaoEncontrado as e:
            return Response(content=str(e), status_code=HTTPStatus.NOT_FOUND)

        except ErroConversaoStrRole as e:
            return Response(content=str(e), status_code=HTTPStatus.BAD_REQUEST)

        except Exception:
            return Response(content="Erro inesperado", status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
