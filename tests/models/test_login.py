import pytest
from pydantic import ValidationError
from src.models.login import Login


class TestLogin:

    def testDefaultPass(self):
        email = "18.00111-1@mail.com"
        senha = "senha"
        login = Login(email=email, senhaEncriptada=senha)
        assert login.email == email
        assert login.senhaEncriptada == senha

    def testValidatorSenhaVazia(self):
        with pytest.raises(ValidationError) as error_info:
            login = Login(email="email@mail.com", senhaEncriptada="")

    def testValidatorEmailVazio(self):
        with pytest.raises(ValidationError) as error_info:
            login = Login(email="", senhaEncriptada="senha")

    def testValidatorEmailInvalido(self):
        with pytest.raises(ValidationError) as error_info:
            login = Login(email="email.mail", senhaEncriptada="senha")