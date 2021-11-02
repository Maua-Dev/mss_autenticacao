from src.models.token import Token
import pytest
from tests.mock_objetos import mockToken


class TestToken:
    token: Token

    @pytest.fixture(autouse=True)
    def rodaAntesDepoisDosTestes(self):
        # setup
        self.token = mockToken()

        yield
        # Teardown

    def testClass(self):
        assert self.token.payload == {"sub": "1234567890","name": "John Doe","iat": 1516239022}
        assert self.token.chave == "your-256-bit-secret"
        assert self.token.algoritmo == "HS256"
        assert self.token.header == {"typ": "JWT"}

    def testClassExceptionFaltaPayload(self):
        with pytest.raises(ValueError) as e:
            token = Token(
                payload={},
                chave=self.token.chave,
                algoritmo=self.token.algoritmo,
                header=self.token.header
            )
            assert str(e) == "Payload Vazio"

    def testClassExceptionFaltaChave(self):
        with pytest.raises(ValueError) as e:
            token = Token(
                payload=self.token.payload,
                chave="",
                algoritmo=self.token.algoritmo,
                header=self.token.header
            )
            assert str(e) == "Chave Vazia"

    def testClassExceptionFaltaAlgoritmo(self):
        with pytest.raises(ValueError) as e:
            token = Token(
                payload=self.token.payload,
                chave=self.token.chave,
                algoritmo="",
                header=self.token.header
            )
            assert str(e) == "Algoritmo Vazio"

    def testClassExceptionFaltaHeader(self):
        with pytest.raises(ValueError) as e:
            token = Token(
                payload=self.token.payload,
                chave=self.token.chave,
                algoritmo=self.token.algoritmo,
                header={}
            )
            assert str(e) == "Header Vazio"

    def testClassCriarDictionary(self):
        dictionary = {
            "payload" : {"sub": "1234567890","name": "John Doe","iat": 1516239022},
            "chave" : "your-256-bit-secret",
            "algoritmo" : "HS256",
            "header" : {"typ": "JWT"}
        }
        token = Token.fromDict(dictionary)
        assert token.payload == dictionary['payload']
