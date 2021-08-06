import jwt

from src.interfaces.i_geracao_token import IGeracaoToken

from src.usecases.errors.erros_uc_criar_jwt import ErroFalhaCriar
from src.usecases.errors.erros_uc_criar_jwt import ErroAlgoritmoVazio
from src.usecases.errors.erros_uc_criar_jwt import ErroSecretVazio
from src.usecases.errors.erros_uc_criar_jwt import ErroPayloadVazio

class UCCriarJWT():
    def __init__(self, jwtRepo: IGeracaoToken):
        self.jwtRepo = jwtRepo

    def __call__(self, payload: dict, secret: str, algorithm: str):
        if not payload:
            raise ErroPayloadVazio
        if not secret:
            raise ErroSecretVazio
        if not algorithm:
            raise ErroAlgoritmoVazio
        try:
            return self.jwtRepo.jwt.encode(payload, secret, algorithm)
        except:
            raise ErroFalhaCriar