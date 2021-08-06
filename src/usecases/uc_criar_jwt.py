import jwt

from src.interfaces.i_geracao_token import IGeracaoToken

class UCCriarJWT():
    def __init__(self, jwtRepo: IGeracaoToken):
        self.jwtRepo = jwtRepo

    def __call__(self, payload: dict, secret: str, algorithm: str):
        try:
            return self.jwtRepo.criarJWT(payload, secret, algorithm)
        except:
            return False