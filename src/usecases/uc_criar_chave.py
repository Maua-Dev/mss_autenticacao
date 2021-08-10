from src.models.m_jwt_chave import ModelJWTChave
from src.interfaces.i_jwt_encriptografar import InterfaceJWTEncriptografar
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import pytest

class UseCaseriarChave():

    interfaceJWTEncriptografar : InterfaceJWTEncriptografar
    
    def __init__(self, interfaceJWTEncriptografar : InterfaceJWTEncriptografar):
        self.interfaceJWTEncriptografar = interfaceJWTEncriptografar
        
    def criarChave(self, jwtDados: ModelJWTChave):
        try:
            private_key = serialization.load_pem_private_key(
                jwtDados.privateChave, password=jwtDados.senha, backend=default_backend()
                )
            return private_key
        except Exception as e:
            raise e