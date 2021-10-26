from typing import Optional
from abc import ABC, abstractmethod
from datetime import date

from src.models.chave import Chave
from src.models.token import Token


class IAuth(ABC):
    
    @abstractmethod
    def criarToken(self, token: Token):
        pass
    
    @abstractmethod
    def criarChave(self, chave: Chave):
        pass
    
    @abstractmethod
    def carregarChave(self):
        pass
    
    @abstractmethod
    def isTokenInvalido(self, token: Token):
        pass

    @abstractmethod
    def isChaveInvalida(self, chave: Chave):
        pass

    @abstractmethod
    def verificarToken(self, response: str):
        pass
