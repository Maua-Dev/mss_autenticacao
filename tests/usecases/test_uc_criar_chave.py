from tests.models.test_model_jwt_chave_encriptografar import JWTChave
from tests.interfaces.test_i_jwt_encriptografar import IJWTEncriptografar
import pytest

class ucCriarJWT():

    iJWTEncriptografar : IJWTEncriptografar
    
    def __init__(self, iJWTEncriptografar : IJWTEncriptografar):
        self.iJWTEncriptografar = iJWTEncriptografar
        
    def criarChave(self, jwtDados: JWTChave):
        self.iJWTEncriptografar.criarChave(jwtDados)