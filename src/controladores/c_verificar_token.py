from fastapi import Response

from src.interfaces.i_auth import IAuth

from src.usecases.uc_criar_token import UCVerificarToken

from fastapi import Response

class CVerificarToken():
    auth: IAuth

    def __init__(self, auth: IAuth):
        self.auth = auth

    def __call__(self, body: str):
        try:
            content = UCVerificarToken(self.auth)(body)
            response = Response(content=str(content), status_code=200)
        except:
            response = Response(content="Error", status_code=400)

        return response

