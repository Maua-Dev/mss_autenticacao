from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login
import bcrypt


class UCLogin():
    usuariosRepo: IArmazenamento

    def __init__(self, usuariosRepo: IArmazenamento):
        self.usuariosRepo = usuariosRepo

    def autenticaLogin(self, login: Login):
        if self.usuariosRepo.emailExiste(login.email):
            if bcrypt.checkpw(login.senha.encode(), self.usuariosRepo.getSenhaEncriptadaPorEmail(login.email).encode()):
                return True
        return False
        #TODO Considerar levantar erro?
