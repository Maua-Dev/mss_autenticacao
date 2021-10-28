from devmaua.src.enum.roles import Roles

from src.repositorios.erros.erros_volatil import ErroEmailNaoEncontrado
from src.repositorios.volatil.armazenamento_volatil import ArmazenamentoUsuarioVolatil
from src.models.login import Login
import pytest


class TestArmazenamentoVolatil:
    armazenamento: ArmazenamentoUsuarioVolatil
    login: Login
    emailErr: str

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):
        #setup
        self.armazenamento = ArmazenamentoUsuarioVolatil()
        self.login = Login(email="18.01234-5@maua.br", senha="test", roles=[Roles.ALUNO])
        self.armazenamento.cadastrarLoginAuth(login=self.login)
        self.emailErr = "18.01111-5@maua.br"

        yield
        # Teardown

    def testEmailExiste(self):
        assert self.armazenamento.emailExiste(self.login.email)

    def testEmailNaoExiste(self):
        testLogin = Login(email=self.emailErr, senha="test")
        assert not self.armazenamento.emailExiste(testLogin.email)

    def testAlterarSenha(self):
        assert self.armazenamento.armazem[0].senha == "test"

        self.armazenamento.alterarSenha(Login(email=self.login.email, senha="alteracao"))
        assert self.armazenamento.armazem[0].senha == "alteracao"
        assert len(self.armazenamento.armazem) == 1

    def testAlterarSenhaErroEmailNaoEncontrado(self):
        with pytest.raises(ErroEmailNaoEncontrado):
            self.armazenamento.alterarSenha(Login(email=self.emailErr, senha="alteracao"))

    def testDeletarLoginAuthPorEmail(self):
        assert len(self.armazenamento.armazem) == 1

        self.armazenamento.deletarLoginAuthPorEmail(self.login.email)

        assert len(self.armazenamento.armazem) == 0

    def testDeletarLoginAuthPorEmailErroEmailNaoEncontrado(self):
        with pytest.raises(ErroEmailNaoEncontrado):
            self.armazenamento.deletarLoginAuthPorEmail(email=self.emailErr)

    def testGetSenhaEncriptadaPorEmail(self):
        assert self.armazenamento.getSenhaEncriptadaPorEmail(self.login.email) == self.login.senha

    def testGetSenhaEncriptadaPorEmailErroEmailNaoEncontrado(self):
        with pytest.raises(ErroEmailNaoEncontrado):
            self.armazenamento.deletarLoginAuthPorEmail(email=self.emailErr)

    def testAtualizarRolesPorEmail(self):
        assert self.armazenamento.armazem[0].roles[0] == Roles.ALUNO

        self.armazenamento.atualizarRolePorEmail(self.login.email, [Roles.ALUNO_IC])

        assert self.armazenamento.armazem[0].roles[0] == Roles.ALUNO_IC

    def testAtualizarRolesPorEmailErroEmailNaoEncontrado(self):
        with pytest.raises(ErroEmailNaoEncontrado):
            self.armazenamento.atualizarRolePorEmail(self.emailErr, [Roles.ALUNO_IC])

    def testGetRolesPorEmail(self):
        self.armazenamento.getRolesPorEmail(self.login.email)

        assert self.armazenamento.armazem[0].roles == [Roles.ALUNO]

    def testGetRolesPorEmailErroEmailNaoEncontrado(self):
        with pytest.raises(ErroEmailNaoEncontrado):
            self.armazenamento.getRolesPorEmail(self.emailErr)
