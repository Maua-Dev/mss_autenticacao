from tests.models.test_model_jwt_token_encriptografar import JWTToken
from tests.interfaces.test_i_jwt_encriptografar import IJWTEncriptografar
import pytest

class ucCriarJWT():

    iJWTEncriptografar : IJWTEncriptografar
    
    def __init__(self, iJWTEncriptografar : IJWTEncriptografar):
        self.iJWTEncriptografar = iJWTEncriptografar
        
    def criarJWT(self, jwtDados: JWTToken, chave: str):
        if not chave:
            raise Exception
        self.iJWTEncriptografar.criarJWT(jwtDados, chave)