
from abc import ABC, abstractmethod


class IOperacoesHash(ABC):

    @abstractmethod
    def checarHashSenha(self, senha: str, hash: str) -> bytes:
        pass

    @abstractmethod
    def criarHashSenha(self, senha: str) -> bytes:
        pass
