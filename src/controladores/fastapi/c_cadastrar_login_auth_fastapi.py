from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login
from src.usecases.uc_usuario_auth import UCUsuarioAuth
from fastapi import Response
from http import HTTPStatus
from src.usecases.erros.erros_uc import ErroEmailJaCadastrado
from src.models.erros.erros_models import ErroEmailVazio, ErroEmailInvalido, ErroSenhaVazio, ErroConversaoRequestLogin
from src.interfaces.i_operacoes_hash import IOperacoesHash


class CCadastrarLoginAuthFastApi():
    repo: IArmazenamento
    uc: UCUsuarioAuth

    def __init__(self, repo: IArmazenamento, iHash: IOperacoesHash):
        self.repo = repo
        self.uc = UCUsuarioAuth(self.repo, iHash)

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

            self.uc.cadastrarLoginAuth(login)

            return Response(content="Cadastrado com sucesso", status_code=HTTPStatus.CREATED)

        except (ErroEmailVazio, ErroEmailInvalido, ErroSenhaVazio, ErroConversaoRequestLogin, ErroEmailJaCadastrado) as e:
            return Response(content=str(e), status_code=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response(content="Erro inesperado", status_code=HTTPStatus.INTERNAL_SERVER_ERROR)

