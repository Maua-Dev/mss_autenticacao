import jwt

from abc import abstractmethod
from dotenv import dotenv_values

from src.models.token import Token
from src.models.chave import Chave

from src.interfaces.i_geracao import IGeracao

from src.repositorios.erros.erros_jwt import ErroCarregarEnv


class JWTGeracao(IGeracao):
    def criarToken(self, token: Token):
        chave = self.carregarChave()
        token = jwt.encode(token.payload, chave, algorithm="HS256", headers={"typ": "JWT"})
        return token

    def criarChave(self, chave: Chave):
        pass
    
    def carregarChave(self):
        try:
            chave = dotenv_values(".env")
            return chave["password"]
        except:
            raise ErroCarregarEnv
    
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