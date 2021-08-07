from typing import Optional
from abc import ABC, abstractmethod
from datetime import date

from tests.models.test_model_jwt_chave_encriptografar import JWTChave
from tests.models.test_model_jwt_token_encriptografar import JWTToken

class IJWTEncriptografar(ABC):
    
    @abstractmethod
    def criarJWT(self, jwtDados: JWTToken, chave: str):
        """ Cria JWT com valores e chave. """
        pass
    
    @abstractmethod
    def criarChave(self, jwtChave: JWTChave):
        """ Cria chave para JWT """
        pass