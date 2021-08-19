from src.models.token import Token
from src.interfaces.i_auth import IAuth


class UCVerificarToken():
    auth: IAuth

    def __init__(self, auth: IAuth):
        self.auth = auth

    def __call__(self, response: String):
        return self.auth.verificarToken(response)