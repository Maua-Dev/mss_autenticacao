from typing import Optional
from abc import ABC, abstractmethod
from datetime import date

from src.models.m_jwt_chave import ModelJWTChave
from src.models.m_jwt_token import ModelJWTToken

class InterfaceJWTEncriptografar(ABC):
    
    @abstractmethod
    def criarJWT(self, modelJWTToken: ModelJWTToken, chave: str):
        """ Cria JWT com valores e chave. """
        pass
    
    @abstractmethod
    def criarChave(self, modelJWTChave: ModelJWTChave):
        """ Cria chave para JWT """
        pass