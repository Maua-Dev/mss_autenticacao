import pytest
import jwt

from src.interfaces.i_jwt_encriptografar import IJWTEncriptografar
from src.models.m_jwt_token import MJWTToken

class UCCriarJWT():

    iJWTEncriptografar : IJWTEncriptografar
    
    def __init__(self, iJWTEncriptografar : IJWTEncriptografar):
        self.iJWTEncriptografar = iJWTEncriptografar
        
    def criarJWT(self, jwtDados: MJWTToken, chave: str):
        if not chave:
            raise Exception
        try:
            encoded = jwt.encode(jwtDados.payload, chave, algorithm=jwtDados.algoritmo, headers=jwtDados.header)
            return encoded
        except:
            raise Exception