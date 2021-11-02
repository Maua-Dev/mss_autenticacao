from src.models.chave import Chave
import pytest
from tests.mock_objetos import mockChave


class TestChave:
    chave: Chave

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):
        # setup
        self.chave = mockChave()

        yield
        # Teardown

    def testClass(self):
        assert self.chave.chavePrivada == "-----BEGIN PRIVATE KEY-----\nMIGEAgEAMBAGByqGSM49AgEGBS..."
        assert self.chave.senha == "your password"

    def testExceptionFaltandoChavePrivada(self):
        with pytest.raises(ValueError) as e:
            Chave(
                chavePrivada= "",
                senha=self.chave.senha,
            )
            assert str(e) == "chavePrivada Vazio"

    def testExceptionFaltandoSenha(self):
        with pytest.raises(ValueError) as e:
            Chave(
                chavePrivada=self.chave.chavePrivada,
                senha="",
            )
            assert str(e) == "Senha Vazio"


