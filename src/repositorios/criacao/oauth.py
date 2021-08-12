from abc import abstractmethod
from dotenv import dotenv_values

from src.models.token import Token
from src.models.chave import Chave

from src.interfaces.i_geracao import IGeracao

from src.repositorios.erros.erros_jwt import ErroCarregarEnv


class OAuthGeracao(IGeracao):
    def criarToken(self, token: Token):
        pass

    def criarChave(self, chave: Chave):
        pass
    
    def carregarChave(self):
        pass
    
    def tokenInvalido(self, token: Token):
        if not token.payload:
            return True
        else:
            return False
    
    def chaveInvalido(self, chave: Chave):
        if not chave.chavePrivada:
            return True
        else:
            return False