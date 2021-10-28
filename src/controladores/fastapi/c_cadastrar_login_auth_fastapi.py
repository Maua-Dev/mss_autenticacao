from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login
from src.usecases.uc_usuario_auth import UCUsuarioAuth
from fastapi import Response, status, HTTPException
from src.usecases.erros.erros_uc import ErroEmailJaCadastrado, ErroInesperado
from src.models.erros.erros_models import ErroEmailVazio, ErroEmailInvalido, ErroSenhaVazio, ErroConversaoRequestLogin
from src.interfaces.i_operacoes_hash import IOperacoesHash
import logging


class CCadastrarLoginAuthFastApi:
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

            return Response(content="Cadastrado com sucesso", status_code=status.HTTP_201_CREATED)

        #TODO considerar: ErroEmailJaCadastrado como 409 Conflict ou deixamos como 400
        except (ErroEmailVazio, ErroEmailInvalido, ErroSenhaVazio, ErroConversaoRequestLogin, ErroEmailJaCadastrado) as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logging.exception(f"{str(ErroInesperado())}: {str(e)}")
            raise HTTPException(detail=str(ErroInesperado()), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

