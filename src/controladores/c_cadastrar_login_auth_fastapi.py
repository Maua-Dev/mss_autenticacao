from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login
from src.usecases.uc_usuario_auth import UCUsuarioAuth
from fastapi import Response
from http import HTTPStatus
from src.usecases.errors.erros_uc import ErroEmailJaCadastrado
from src.models.erros.erros_models import ErroEmailVazio, ErroEmailInvalido, ErroSenhaVazio, ErroConversaoRequestLogin


class CCadastrarLoginAuthFastApi():
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
            'senha': senha
        }
        """
        try:
            login = Login.fromDict(body)

            self.uc.cadastraLoginAuth(login)

            return Response(content="Cadastrado com sucesso", status_code=HTTPStatus.CREATED)

        except (ErroEmailVazio, ErroEmailInvalido, ErroSenhaVazio, ErroConversaoRequestLogin, ErroEmailJaCadastrado) as e:
            return Response(content=str(e), status_code=HTTPStatus.BAD_REQUEST)

        except Exception:
            return Response(content="Erro inesperado", status_code=HTTPStatus.INTERNAL_SERVER_ERROR)

