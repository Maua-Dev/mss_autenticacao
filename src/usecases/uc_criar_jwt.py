import pytest
import jwt

from src.interfaces.i_jwt_encriptografar import InterfaceJWTEncriptografar
from src.models.m_jwt_token import ModelJWTToken

class UseCaseCriarJWT():

    iJWTEncriptografar : InterfaceJWTEncriptografar
    
    def __init__(self, interfaceJWTEncriptografar : InterfaceJWTEncriptografar):
        self.interfaceJWTEncriptografar = interfaceJWTEncriptografar
        
    def criarJWT(self, modelJWTToken: ModelJWTToken, chave: str):
        if not chave:
            raise Exception
        try:
            encoded = jwt.encode(modelJWTToken.payload, chave, algorithm=modelJWTToken.algoritmo, headers=modelJWTToken.header)
            return encoded
        except:
            raise Exception