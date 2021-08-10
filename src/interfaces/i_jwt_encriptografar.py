from typing import Optional
from abc import ABC, abstractmethod
from datetime import date

from src.models.m_jwt_chave import JWTChave
from src.models.m_jwt_token import JWTToken

class IJWTEncriptografar(ABC):
    
    @abstractmethod
    def criarJWT(self, modelJWTToken: JWTToken, chave: str):
        """ Cria JWT com valores e chave. """
        pass
    
    @abstractmethod
    def criarChave(self, modelJWTChave: JWTChave):
        """ Cria chave para JWT """
        pass