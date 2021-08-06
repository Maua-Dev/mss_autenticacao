from abc import ABC, abstractmethod


class IGeracaoToken(ABC):
    @abstractmethod
    def criarJWT(self, payload: dict, secret: str, algorithm: str):
        pass