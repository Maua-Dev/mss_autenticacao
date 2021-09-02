from devmaua.src.enum.roles import Roles

from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login


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

    # TODO Considerar se é melhorar retornar Erro
    # Passado Login, com email e hashSenhaNova
    def alterarSenha(self, login: Login):
        for l in self.armazem:
            if l.email == login.email:
                l.senha = login.senha
                return True;
        return False

    def deletarLoginAuthPorEmail(self, email: str):
        for i in range(len(self.armazem)):
            if self.armazem[i].email == email:
                del self.armazem[i]
                return True
        return False

    def getSenhaEncriptadaPorEmail(self, email: str):
        for l in self.armazem:
            if l.email == email:
                return l.senha

    def atualizaRolePorEmail(self, email:str, roles: list[Roles]):
        for l in self.armazem:
            if l.email == email:
                l.atualizaRoles(roles)
                return True
        return False
