from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login
from src.interfaces.i_operacoes_hash import IOperacoesHash
from .erros.erros_uc import ErroEmailEOuSenhaIncorretos


class UCLogin:
    usuariosRepo: IArmazenamento
    iHash: IOperacoesHash

    def __init__(self, usuariosRepo: IArmazenamento, iHash: IOperacoesHash):
        self.usuariosRepo = usuariosRepo
        self.iHash = iHash

    def autenticarLogin(self, login: Login):
        if self.usuariosRepo.emailExiste(login.email):
            if self.iHash.checarHashSenha(login.senha, self.usuariosRepo.getSenhaEncriptadaPorEmail(login.email)):
                return True
        raise ErroEmailEOuSenhaIncorretos
