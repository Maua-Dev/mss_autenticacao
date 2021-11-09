from src.interfaces.i_auth import IAuth

from src.usecases.uc_verificar_token import UCVerificarToken

from fastapi import Response, status, HTTPException


class CVerificarTokenFastAPI:
    auth: IAuth

    def __init__(self, auth: IAuth):
        self.auth = auth

    def __call__(self, body: str):
        try:
            content = UCVerificarToken(self.auth)(body)
            return Response(content=str(content), status_code=status.HTTP_200_OK)
        except Exception as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_401_UNAUTHORIZED)

