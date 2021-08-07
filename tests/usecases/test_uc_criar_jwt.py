from tests.models.test_model_jwt_token_encriptografar import JWTToken
from tests.interfaces.test_i_jwt_encriptografar import IJWTEncriptografar
import pytest
import jwt

class ucCriarJWT():

    iJWTEncriptografar : IJWTEncriptografar
    
    def __init__(self, iJWTEncriptografar : IJWTEncriptografar):
        self.iJWTEncriptografar = iJWTEncriptografar
        
    def criarJWT(self, jwtDados: JWTToken, chave: str):
        if not chave:
            raise Exception
        try:
            encoded = jwt.encode(jwtDados.payload, chave, algorithm=jwtDados.algoritmo, headers=jwtDados.header)
            return encoded
        except:
            raise Exception