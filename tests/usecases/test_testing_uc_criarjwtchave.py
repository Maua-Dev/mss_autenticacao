from tests.usecases.test_uc_criar_chave import ucCriarChave
from tests.usecases.test_uc_criar_jwt import ucCriarJWT
from tests.models.test_model_jwt_chave_encriptografar import JWTChave
from tests.models.test_model_jwt_token_encriptografar import JWTToken
from tests.interfaces.test_i_jwt_encriptografar import IJWTEncriptografar
import pytest

from cryptography.hazmat.primitives.asymmetric import rsa

@pytest.mark.xfail
def testeCriarChave(): #Tofix
    modulus_length = 1024
    
    private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048).private_bytes("PEM", "Raw, ")

    chave = JWTChave(
        privateChave= private_key,
        senha= b"Unguessable",
        )
    chaveCriada = ucCriarChave(IJWTEncriptografar).criarChave(chave)
    
def testeCriarToken():
    tokenModel = JWTToken(
        payload={"sub": "1234567890","name": "John Doe","iat": 1516239022},
        chave="your-256-bit-secret",
        algoritmo="HS256",
        header={"typ": "JWT"}
        )
    token = ucCriarJWT(IJWTEncriptografar).criarJWT(tokenModel, "secret")
    