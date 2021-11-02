from devmaua.src.enum.roles import Roles

from src.models.login import Login
from src.models.token import Token
from src.models.chave import Chave


def mockToken() -> Token:
    # Usando valores default de jwt.io, convertidos
    return Token(
        payload={"sub": "1234567890","name": "John Doe","iat": 1516239022},
        chave="your-256-bit-secret",
        algoritmo="HS256",
        header={"typ": "JWT"}
        )


def mockChave() -> Chave:
    # Usando valores default de jwt.io, convertidos
    return Chave(
        chavePrivada=b"-----BEGIN PRIVATE KEY-----\nMIGEAgEAMBAGByqGSM49AgEGBS...",
        senha=b"your password",
    )


def mockLogin() -> Login:
    return Login(email="18.01234-5@maua.br", senha="senha", roles=[Roles.ALUNO])