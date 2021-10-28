from typing import List

from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login
from src.interfaces.i_operacoes_hash import IOperacoesHash
from devmaua.src.enum.roles import Roles
from .erros.erros_uc import *


class UCUsuarioAuth:
    armazenamento: IArmazenamento
    iHash: IOperacoesHash

    def __init__(self, armazenamento: IArmazenamento, iHash: IOperacoesHash = None):
        self.armazenamento = armazenamento
        self.iHash = iHash

    def cadastrarLoginAuth(self, login: Login):
        if self.armazenamento.emailExiste(login.email):
            raise ErroEmailJaCadastrado

        #Faz decode() do hash para salvar no db como string e nao byte
        loginEncriptado = Login(email=login.email, senha=self.iHash.criarHashSenha(login.senha).decode(), roles=login.roles)
        self.armazenamento.cadastrarLoginAuth(loginEncriptado)

    def deletarLoginPorEmail(self, email: str):
        self.armazenamento.deletarLoginAuthPorEmail(email)

    def alterarSenha(self, login: Login):
        #Faz decode do hash para salvar no db como string
        loginEncriptado = Login(email=login.email, senha=self.iHash.criarHashSenha(login.senha).decode(), roles=login.roles)
        self.armazenamento.alterarSenha(loginEncriptado)

    def atualizarRoles(self, email: str, roles: list[Roles]):
        self.armazenamento.atualizarRolePorEmail(email, roles)

    def getRolesPorEmail(self, email: str) -> List[Roles]:
        return self.armazenamento.getRolesPorEmail(email)
