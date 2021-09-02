from src.usecases.uc_login import UCLogin
from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login
from fastapi import Response

class CLogarFastApi():
    repo: IArmazenamento
    uc: UCLogin

    def __init__(self, repo: IArmazenamento):
        self.repo = repo
        self.uc = UCLogin(self.repo)

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
            if self.uc.autenticaLogin(login):
                # cria jwt
                content = "JWT"
            #TODO Considerar trocar Response para um model response que tenha mensagem e codigo -> Paramos de depender do FastApi
            return Response(content=content, status_code=200)
        except:
            return Response(content="Erro", status_code=500)
            #TODO Considerar: Adicionar tipo enum para status codes e erros para auth