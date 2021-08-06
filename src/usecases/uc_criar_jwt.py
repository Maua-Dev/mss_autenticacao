import jwt

from src.interfaces.i_geracao_token import IGeracaoToken

from src.usecases.errors.erros_uc_criar_jwt import ErroFalhaCriar
from src.usecases.errors.erros_uc_criar_jwt import ErroAlgoritmoVazio
from src.usecases.errors.erros_uc_criar_jwt import ErroSecretVazio
from src.usecases.errors.erros_uc_criar_jwt import ErroPayloadVazio

class UCCriarJWT():

    def __init__(self, payload: dict, secret: str, algorithm: str):
        self.payload = payload
        self.secret = secret
        self.algorithm = algorithm

    def __call__(self):
        if not self.payload:
            raise ErroPayloadVazio
        if not self.secret:
            raise ErroSecretVazio
        if not self.algorithm:
            raise ErroAlgoritmoVazio
        try:
            return self.jwtRepo.jwt.encode(self.payload, self.secret, self.algorithm)
        except:
            raise ErroFalhaCriar