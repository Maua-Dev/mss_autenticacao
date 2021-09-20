from devmaua.src.enum.roles import Roles

from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login
from src.repositorios.erros.erros_volatil import ErroEmailNaoEncontrado

class ArmazenamentoUsuarioVolatil(IArmazenamento):

    armazem: list[Login]

    def __init__(self):
        self.armazem = []

    def emailExiste(self, email: str):
        for l in self.armazem:
            if l.email == email:
                return True
        return False

    def cadastrarLoginAuth(self, login: Login):
        self.armazem.append(login)

    # Passado Login, com email e hashSenhaNova
    def alterarSenha(self, login: Login):
        for l in self.armazem:
            if l.email == login.email:
                l.senha = login.senha
                return True
        raise ErroEmailNaoEncontrado

    def deletarLoginAuthPorEmail(self, email: str):
        for i in range(len(self.armazem)):
            if self.armazem[i].email == email:
                del self.armazem[i]
                return True
        raise ErroEmailNaoEncontrado

    def getSenhaEncriptadaPorEmail(self, email: str):
        for l in self.armazem:
            if l.email == email:
                return l.senha
        raise ErroEmailNaoEncontrado

    def atualizarRolePorEmail(self, email: str, roles: list[Roles]):
        for l in self.armazem:
            if l.email == email:
                l.atualizarRoles(roles)
                return True
        raise ErroEmailNaoEncontrado

    def getRolesPorEmail(self, email: str):
        for l in self.armazem:
            if l.email == email:
                return l.roles
        raise ErroEmailNaoEncontrado
