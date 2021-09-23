from src.repositorios.volatil.armazenamento_volatil import ArmazenamentoUsuarioVolatil
from src.models.login import Login
import pytest


class TestArmazenamentoVolatil:
    armazenamento: ArmazenamentoUsuarioVolatil
    login: Login

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):

        #setup
        self.armazenamento = ArmazenamentoUsuarioVolatil()
        self.login = Login(email="18.01234-5@maua.br", senha="test")
        self.armazenamento.cadastrarLoginAuth(login=self.login)

        yield

        # Teardown


    def testEmailExiste(self):
        assert self.armazenamento.emailExiste(self.login.email)


    def testAlterarSenha(self):
        assert self.armazenamento.armazem[0].senha == "test"

        self.armazenamento.alterarSenha(Login(email=self.login.email, senha="alteracao"))
        assert self.armazenamento.armazem[0].senha == "alteracao"
        assert len(self.armazenamento.armazem) == 1

    def testDeletarLoginAuthPorEmail(self):
        assert len(self.armazenamento.armazem) == 1

        self.armazenamento.deletarLoginAuthPorEmail(self.login.email)

        assert len(self.armazenamento.armazem) == 0

    def testGetSenhaEncriptada(self):
        assert self.armazenamento.getSenhaEncriptadaPorEmail(self.login.email) == self.login.senha