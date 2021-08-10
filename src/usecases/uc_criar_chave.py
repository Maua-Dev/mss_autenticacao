from src.models.m_jwt_chave import ModelJWTChave
from src.interfaces.i_jwt_encriptografar import InterfaceJWTEncriptografar
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import pytest

class UseCaseCriarChave():

    interfaceJWTEncriptografar : InterfaceJWTEncriptografar
    
    def __init__(self, interfaceJWTEncriptografar : InterfaceJWTEncriptografar):
        self.interfaceJWTEncriptografar = interfaceJWTEncriptografar
        
    def criarChave(self, modelJWTChave: ModelJWTChave):
        try:
            private_key = serialization.load_pem_private_key(
                modelJWTChave.privateChave, password=modelJWTChave.senha, backend=default_backend()
                )
            return private_key
        except Exception as e:
            raise e