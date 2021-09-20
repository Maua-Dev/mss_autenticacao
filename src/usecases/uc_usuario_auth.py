from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login
import bcrypt
from devmaua.src.enum.roles import Roles
from .errors.erros_uc import *

class UCUsuarioAuth:
    armazenamento: IArmazenamento

    def __init__(self, armazenamento: IArmazenamento):
        self.armazenamento = armazenamento

    def cadastrarLoginAuth(self, login: Login):
        if self.armazenamento.emailExiste(login.email):
            raise ErroEmailJaCadastrado

        #Faz decode() do hash para salvar no db como string e nao byte
        loginEncriptado = Login(email=login.email, senha=self._encriptarSenha(login.senha).decode())
        self.armazenamento.cadastrarLoginAuth(loginEncriptado)

    def deletarLoginPorEmail(self, email: str):
        self.armazenamento.deletarLoginAuthPorEmail(email)

    def alterarSenha(self, login: Login):
        #Faz decode do hash para salvar no db como string
        loginEncriptado = Login(email=login.email, senha=self._encriptarSenha(login.senha).decode())
        self.armazenamento.alterarSenha(loginEncriptado)

    def atualizarRoles(self, email: str, roles: list[Roles]):
        self.armazenamento.atualizarRolePorEmail(email, roles)

    def getRolesPorEmail(self, email: str):
        return self.armazenamento.getRolesPorEmail(email)

    def _encriptarSenha(self, senha: str):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(senha.encode(), salt)
