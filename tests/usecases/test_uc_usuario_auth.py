import pytest
from src.repositorios.volatil.armazenamento_volatil import ArmazenamentoUsuarioVolatil
from src.models.login import Login
from src.usecases.uc_usuario_auth import UCUsuarioAuth
import bcrypt
from devmaua.src.enum.roles import Roles
from src.controladores.hashing.bcrypt.c_operacoes_bcrypt import COperacoesBcrypt
from src.usecases.erros.erros_uc import ErroEmailJaCadastrado


class TestUCUsuarioAuth:
    armazenamento: ArmazenamentoUsuarioVolatil
    login: Login
    uc: UCUsuarioAuth

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):
        # setup
        self.armazenamento = ArmazenamentoUsuarioVolatil()
        self.login = Login(email="18.01234-5@maua.br", senha="senha", roles=[Roles.ALUNO])
        self.uc = UCUsuarioAuth(self.armazenamento, COperacoesBcrypt())

        self.uc.cadastrarLoginAuth(self.login)

        yield
        # Teardown

    def testCadastrarLoginAuth(self):
        assert self.login.email == self.armazenamento.armazem[0].email
        # hash senha verificada depois -> testando aqui que ela existe
        assert self.armazenamento.armazem[0].senha
        assert self.login.roles == self.armazenamento.armazem[0].roles


    def testCadastrarLoginLevantaErroComEmailIgual(self):
        with pytest.raises(ErroEmailJaCadastrado):
            self.uc.cadastrarLoginAuth(self.login)

    def testCadastrarLoginFazHashDaSenha(self):
        assert bcrypt.checkpw("senha".encode(), self.armazenamento.armazem[0].senha.encode())

    def testDeletarLoginPorEmail(self):
        adicionado = len(self.armazenamento.armazem) == 1

        self.uc.deletarLoginPorEmail("18.01234-5@maua.br")

        deletado = len(self.armazenamento.armazem) == 0

        assert adicionado and deletado

    def testAlterarSenha(self):
        self.uc.alterarSenha(Login(email=self.login.email, senha="SenhaAlterada"))

        assert self.login.email == self.armazenamento.armazem[0].email
        # hash senha verificada depois -> testando aqui que ela existe
        assert self.armazenamento.armazem[0].senha
        assert self.login.roles == self.armazenamento.armazem[0].roles

    def testAlterarSenhaFazHashDaSenha(self):
        self.uc.alterarSenha(Login(email=self.login.email, senha="SenhaAlterada"))

        assert bcrypt.checkpw("SenhaAlterada".encode(), self.armazenamento.armazem[0].senha.encode())

    def testAtualizarRolesPorEmail(self):
        padrao = self.armazenamento.armazem[0].roles == self.login.roles

        roles = [Roles.ALUNO, Roles.MONITOR_DISCIPLINA]

        self.uc.atualizarRoles(self.login.email, roles)

        esperado = self.armazenamento.armazem[0].roles == roles

        assert padrao and esperado

    def testGetRolesPorEmail(self):
        roles = self.uc.getRolesPorEmail(self.login.email)
        assert roles == self.login.roles
