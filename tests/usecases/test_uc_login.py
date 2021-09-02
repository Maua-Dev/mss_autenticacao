import pytest
from src.repositorios.volatil.armazenamento_volatil import ArmazenamentoUsuarioVolatil
from src.models.login import Login
from src.usecases.uc_login import UCLogin
import bcrypt


class TestUCLogin:
    armazenamento: ArmazenamentoUsuarioVolatil
    login: Login
    uc: UCLogin

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):
        # setup
        self.armazenamento = ArmazenamentoUsuarioVolatil()
        self.login = Login(email="18.01234-5@maua.br", senha=bcrypt.hashpw(b"senha", bcrypt.gensalt()))
        self.armazenamento.cadastrarLoginAuth(login=self.login)
        self.uc = UCLogin(self.armazenamento)
        yield
        # Teardown

    def testPadraoPassa(self):
        loginCorreto = Login(email="18.01234-5@maua.br", senha="senha")
        assert self.uc.autenticaLogin(loginCorreto)

    def testFalhaNoEmail(self):
        loginEmailErrado = Login(email="17.01234-5@maua.br", senha="senha")
        assert not self.uc.autenticaLogin(loginEmailErrado)

    def testFalhaNaSenha(self):
        loginSenhaErrada = Login(email="18.01234-5@maua.br", senha="sEnha")
        assert not self.uc.autenticaLogin(loginSenhaErrada)