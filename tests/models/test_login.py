import pytest
from pydantic import ValidationError
from src.models.login import Login
from src.models.erros.erros_models import ErroEmailVazio, ErroEmailInvalido, ErroSenhaVazio, ErroConversaoRequestLogin, ErroConversaoStrRole
from devmaua.src.enum.roles import Roles



class TestLogin:

    def testDefaultPass(self):
        email = "18.00111-1@mail.com"
        senha = "senha"
        login = Login(email=email, senha=senha)
        assert login.email == email
        assert login.senha == senha

    def testValidatorSenhaVazia(self):
        with pytest.raises(ErroSenhaVazio):
            login = Login(email="email@mail.com", senha="")

    def testValidatorEmailVazio(self):
        with pytest.raises(ErroEmailVazio):
            login = Login(email="", senha="senha")

    def testValidatorEmailInvalido(self):
        with pytest.raises(ErroEmailInvalido):
            login = Login(email="email.mail", senha="senha")

# === fromDict()
    def testConversaoDictJogaErroSenhaVazia(self):
        with pytest.raises(ErroSenhaVazio):
            Login.fromDict({"email": "mail@mail.com", "senha": ""})
    def testConversaoDictJogaErroEmailVazio(self):
        with pytest.raises(ErroEmailVazio):
            Login.fromDict({"email": "", "senha": "senha"})
    def testConversaoDictJogaErroEmailInvalido(self):
        with pytest.raises(ErroEmailInvalido):
            Login.fromDict({"email": "mail.mail.com", "senha": "senha"})
    def testConversaoDictJogaErroDeConversaoDict(self):
        with pytest.raises(ErroConversaoRequestLogin):
            # ocorre quando o corpo nao esta no formato {"email":"", "senha":""}
            Login.fromDict({"eail": "mail@mail.com", "senha": "senha"})
# ===

    def testRolesFromStrListPadrao(self):
        roles = Login.rolesFromStrList(["ALUNo", "PROFESSOR"])

        assert roles[0] == Roles.ALUNO and roles[1] == Roles.PROFESSOR

    def testRolesFromStrListErro(self):
        with pytest.raises(ErroConversaoStrRole):
            Login.rolesFromStrList(["INEXISTENTE"])