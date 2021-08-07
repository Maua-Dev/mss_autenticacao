from tests.models.test_jwt_token import JWTToken
import pytest

def testClass():
    # Usando valores default de jwt.io, convertidos
    jWTToken = JWTToken()
    jWTToken = jWTToken.criarToken(
        payload={"sub": "1234567890","name": "John Doe","iat": 1516239022},
        chave="your-256-bit-secret",
        algoritmo="HS256",
        header={"typ": "JWT",}
        )
    
    assert jWTToken == "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.wrJ__8Q_6BcB2ug9370TBuK5JoAjErqsQtYf7aLcFBk"
    
def testClassExceptionFaltaHeader():
    with pytest.raises(Exception) as ValueError:
        jWTToken = JWTToken()
        jWTToken = jWTToken.criarToken(
            payload={"sub": "1234567890","name": "John Doe","iat": 1516239022},
            chave="your-256-bit-secret",
            algoritmo="HS256",
            header={}
            )
    
def testClassExceptionFaltaAlgoritmo():
    with pytest.raises(Exception) as ValueError:
        jWTToken = JWTToken()
        jWTToken = jWTToken.criarToken(
            payload={"sub": "1234567890","name": "John Doe","iat": 1516239022},
            chave="your-256-bit-secret",
            algoritmo="",
            header={"typ": "JWT",}
            )

def testClassExceptionFaltaChave():
    with pytest.raises(Exception) as ValueError:
        jWTToken = JWTToken()
        jWTToken = jWTToken.criarToken(
            payload={"sub": "1234567890","name": "John Doe","iat": 1516239022},
            chave="",
            algoritmo="HS256",
            header={"typ": "JWT",}
            )
    
def testClassExceptionFaltaPayload():
    with pytest.raises(Exception) as ValueError:
        jWTToken = JWTToken()
        jWTToken = jWTToken.criarToken(
            payload={},
            chave="your-256-bit-secret",
            algoritmo="HS256",
            header={"typ": "JWT",}
            )
    
    
