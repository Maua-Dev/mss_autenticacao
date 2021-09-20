
from abc import ABC, abstractmethod
from src.models.login import Login
from devmaua.src.enum.roles import Roles


class IArmazenamento(ABC):
    """"
    Interface com os métodos necessários para o gerenciamento de usuários na autenticação
    """
    @abstractmethod
    def emailExiste(self, email: str):
        pass

    @abstractmethod
    def cadastrarLoginAuth(self, login: Login):
        pass

    @abstractmethod
    def alterarSenha(self, login: Login):
        pass

    @abstractmethod
    def deletarLoginAuthPorEmail(self, email: str):
        pass

    @abstractmethod
    def getSenhaEncriptadaPorEmail(self, email: str):
        pass

    @abstractmethod
    def atualizarRolePorEmail(self, email: str, roles: list[Roles]):
        pass

    @abstractmethod
    def getRolesPorEmail(self, email: str):
        pass
