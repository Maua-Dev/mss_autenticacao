from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login
import bcrypt
from devmaua.src.enum.roles import Roles


class UCUsuarioAuth:
    armazenamento: IArmazenamento

    def __init__(self, armazenamento: IArmazenamento):
        self.armazenamento = armazenamento

    def cadastraLoginAuth(self, login: Login):
        if self.armazenamento.emailExiste(login.email):
            raise Exception

        #Faz decode do hash para salvar no db como string
        loginEncriptado = Login(email=login.email, senha=self._encriptaSenha(login.senha).decode())
        self.armazenamento.cadastrarLoginAuth(loginEncriptado)

    def deletaLoginPorEmail(self, email: str):
        self.armazenamento.deletarLoginAuthPorEmail(email)

    def alteraSenha(self, login: Login):
        #Faz decode do hash para salvar no db como string
        loginEncriptado = Login(email=login.email, senha=self._encriptaSenha(login.senha).decode())
        self.armazenamento.alterarSenha(loginEncriptado)

    def atualizaRoles(self, email: str, roles: list[Roles]):
        self.armazenamento.atualizaRolePorEmail(email, roles)

    def _encriptaSenha(self, senha: str):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(senha.encode(), salt)
