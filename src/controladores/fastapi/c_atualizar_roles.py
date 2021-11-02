from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.usecases.uc_usuario_auth import UCUsuarioAuth
from fastapi import Response, status, HTTPException
from src.models.login import Login
from src.repositorios.erros.erros_volatil import ErroEmailNaoEncontrado
from src.models.erros.erros_models import ErroConversaoStrRole
from src.usecases.erros.erros_uc import ErroInesperado
import logging


class CAtualizarRolesFastApi:
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
            self.uc.atualizarRoles(email=body["email"], roles=roles)

            return Response(content="atualizado com sucesso", status_code=status.HTTP_200_OK)

        except ErroEmailNaoEncontrado as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_404_NOT_FOUND)

        except ErroConversaoStrRole as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logging.exception(f"{str(ErroInesperado())}: {str(e)}")
            raise HTTPException(detail=str(ErroInesperado()), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


