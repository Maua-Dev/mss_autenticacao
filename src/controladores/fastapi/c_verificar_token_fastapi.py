from src.interfaces.i_auth import IAuth

from src.usecases.uc_verificar_token import UCVerificarToken

from fastapi import Response, status


class CVerificarTokenFastAPI:
    auth: IAuth

    def __init__(self, auth: IAuth):
        self.auth = auth

    def __call__(self, body: str):
        try:
            content = UCVerificarToken(self.auth)(body)
            response = Response(content=str(content), status_code=status.HTTP_200_OK)
        except Exception as e:
            response = Response(content="Erro Auth", status_code=status.HTTP_401_UNAUTHORIZED)

        return response

