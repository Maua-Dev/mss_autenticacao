from tests.models.test_model_jwt_token_encriptografar import JWTToken
import pytest

def testClass():
    # Usando valores default de jwt.io, convertidos
    jWTToken = JWTToken(
        payload={"sub": "1234567890","name": "John Doe","iat": 1516239022},
        chave="your-256-bit-secret",
        algoritmo="HS256",
        header={"typ": "JWT"}
        )
    
    assert jWTToken.payload == {"sub": "1234567890","name": "John Doe","iat": 1516239022}
    assert jWTToken.chave == "your-256-bit-secret"
    assert jWTToken.algoritmo == "HS256"
    assert jWTToken.header == {"typ": "JWT"}
    
def testClassExceptionFaltaPayload():
    with pytest.raises(Exception) as ValueError:
        jWTToken = JWTToken(
            payload={},
            chave="your-256-bit-secret",
            algoritmo="HS256",
            header={"typ": "JWT"}
        )

def testClassExceptionFaltaChave():
    with pytest.raises(Exception) as ValueError:
        jWTToken = JWTToken(
            payload={"sub": "1234567890","name": "John Doe","iat": 1516239022},
            chave="",
            algoritmo="HS256",
            header={"typ": "JWT"}
        )
        
def testClassExceptionFaltaAlgoritmo():
    with pytest.raises(Exception) as ValueError:
        jWTToken = JWTToken(
            payload={"sub": "1234567890","name": "John Doe","iat": 1516239022},
            chave="your-256-bit-secret",
            algoritmo="",
            header={"typ": "JWT"}
        )
        
def testClassExceptionFaltaHeader():
    with pytest.raises(Exception) as ValueError:
        jWTToken = JWTToken(
            payload={"sub": "1234567890","name": "John Doe","iat": 1516239022},
            chave="your-256-bit-secret",
            algoritmo="HS256",
            header={}
        )
    



    

    
