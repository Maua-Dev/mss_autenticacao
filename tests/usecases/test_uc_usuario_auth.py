import pytest
from src.repositorios.volatil.armazenamento_volatil import ArmazenamentoUsuarioVolatil
from src.models.login import Login
from src.usecases.uc_usuario_auth import UCUsuarioAuth
import bcrypt


class TestUCUsuarioAuth:
    armazenamento: ArmazenamentoUsuarioVolatil
    login: Login
    uc: UCUsuarioAuth

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):
        # setup
        self.armazenamento = ArmazenamentoUsuarioVolatil()
        self.login = Login(email="18.01234-5@maua.br", senha="senha")
        self.uc = UCUsuarioAuth(self.armazenamento)
        yield
        # Teardown

    def testCadastraLoginFazHashDaSenha(self):
        self.uc.cadastraLoginAuth(self.login)
        assert bcrypt.checkpw("senha".encode(), self.armazenamento.armazem[0].senha.encode())

    def testDeletaLoginPorEmail(self):
        self.armazenamento.cadastrarLoginAuth(self.login)
        adicionado = len(self.armazenamento.armazem) == 1

        self.uc.deletaLoginPorEmail("18.01234-5@maua.br")

        deletado = len(self.armazenamento.armazem) == 0

        assert adicionado and deletado

    def testAlteraSenhaFazHashDaSenha(self):
        self.armazenamento.cadastrarLoginAuth(self.login)

        self.uc.alteraSenha(Login(email=self.login.email, senha="SenhaAlterada"))

        assert bcrypt.checkpw("SenhaAlterada".encode(), self.armazenamento.armazem[0].senha.encode())
