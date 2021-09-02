from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.usecases.uc_usuario_auth import UCUsuarioAuth
from fastapi import Response
from src.models.login import Login


class CAtualizarRolesFastApi():
    repo: IArmazenamento
    uc: UCUsuarioAuth

    def __init__(self, repo: IArmazenamento):
        self.repo = repo
        self.uc = UCUsuarioAuth(self.repo)

    def __call__(self, body: dict):
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

        # TODO Considerar: Adicionar tipo enum para status codes e erros para auth
        except ValueError as e:
            return Response(content="Erro na requisicao", status_code=400)
        except Exception:
            return Response(content="Erro", status_code=500)
