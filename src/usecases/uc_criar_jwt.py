import jwt

from src.interfaces.i_jwt_encriptografar import IJWTEncriptografar
from src.models.m_jwt_token import JWTToken

class UCCriarJWT():

    iJWTEncriptografar : IJWTEncriptografar
    
    def __init__(self, iJWTEncriptografar : IJWTEncriptografar):
        self.iJWTEncriptografar = iJWTEncriptografar
        
    def criarJWT(self, modelJWTToken: JWTToken, chave: str):
        if not chave:
            raise Exception
        try:
            encoded = jwt.encode(modelJWTToken.payload, chave, algorithm=modelJWTToken.algoritmo, headers=modelJWTToken.header)
            return encoded
        except:
            raise Exception