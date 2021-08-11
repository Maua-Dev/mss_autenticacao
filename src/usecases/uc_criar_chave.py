from src.models.m_jwt_chave import JWTChave
from src.interfaces.i_jwt_encriptografar import IJWTEncriptografar
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


class UCCriarChave():

    iJWTEncriptografar : IJWTEncriptografar
    
    def __init__(self, iJWTEncriptografar : IJWTEncriptografar):
        self.iJWTEncriptografar = iJWTEncriptografar
        
    def criarChave(self):
        try:
            private_key = ""
            
            return private_key
        except Exception as e:
            raise e