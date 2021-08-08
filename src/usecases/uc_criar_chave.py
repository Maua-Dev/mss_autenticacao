from src.models.m_jwt_chave import MJWTChave
from src.interfaces.i_jwt_encriptografar import IJWTEncriptografar
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import pytest

class UCCriarChave():

    iJWTEncriptografar : IJWTEncriptografar
    
    def __init__(self, iJWTEncriptografar : IJWTEncriptografar):
        self.iJWTEncriptografar = iJWTEncriptografar
        
    def criarChave(self, jwtDados: MJWTChave):
        try:
            private_key = serialization.load_pem_private_key(
                jwtDados.privateChave, password=jwtDados.senha, backend=default_backend()
                )
            return private_key
        except Exception as e:
            raise e