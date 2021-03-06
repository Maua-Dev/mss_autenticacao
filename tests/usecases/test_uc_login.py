import pytest
from src.repositorios.volatil.armazenamento_volatil import ArmazenamentoUsuarioVolatil
from src.models.login import Login
from src.usecases.uc_login import UCLogin
import bcrypt
from src.usecases.erros.erros_uc import ErroEmailEOuSenhaIncorretos
from src.controladores.hashing.bcrypt.c_operacoes_bcrypt import COperacoesBcrypt


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
        self.uc = UCLogin(self.armazenamento, COperacoesBcrypt())
        yield
        # Teardown

    def testPadraoPassa(self):
        loginCorreto = Login(email="18.01234-5@maua.br", senha="senha")
        assert self.uc.autenticarLogin(loginCorreto)

    def testFalhaEmailIncorreto(self):
        with pytest.raises(ErroEmailEOuSenhaIncorretos):
            loginEmailErrado = Login(email="17.01234-5@maua.br", senha="senha")
            self.uc.autenticarLogin(loginEmailErrado)

    def testFalhaSenhaIncorreta(self):
        with pytest.raises(ErroEmailEOuSenhaIncorretos):
            loginSenhaErrada = Login(email="18.01234-5@maua.br", senha="sEnha")
            self.uc.autenticarLogin(loginSenhaErrada)
