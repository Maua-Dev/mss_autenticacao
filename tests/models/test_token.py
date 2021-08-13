from src.models.token import Token
import pytest

def testClass():
    # Usando valores default de jwt.io, convertidos
    token = Token(
        payload={"sub": "1234567890","name": "John Doe","iat": 1516239022},
        chave="your-256-bit-secret",
        algoritmo="HS256",
        header={"typ": "JWT"}
        )
    
    assert token.payload == {"sub": "1234567890","name": "John Doe","iat": 1516239022}
    assert token.chave == "your-256-bit-secret"
    assert token.algoritmo == "HS256"
    assert token.header == {"typ": "JWT"}
    
def testClassExceptionFaltaPayload():
    with pytest.raises(Exception) as ValueError:
        token = Token(
            payload={},
            chave="your-256-bit-secret",
            algoritmo="HS256",
            header={"typ": "JWT"}
        )

def testClassExceptionFaltaChave():
    with pytest.raises(Exception) as ValueError:
        token = Token(
            payload={"sub": "1234567890","name": "John Doe","iat": 1516239022},
            chave="",
            algoritmo="HS256",
            header={"typ": "JWT"}
        )
        
def testClassExceptionFaltaAlgoritmo():
    with pytest.raises(Exception) as ValueError:
        token = Token(
            payload={"sub": "1234567890","name": "John Doe","iat": 1516239022},
            chave="your-256-bit-secret",
            algoritmo="",
            header={"typ": "JWT"}
        )
        
def testClassExceptionFaltaHeader():
    with pytest.raises(Exception) as ValueError:
        token = Token(
            payload={"sub": "1234567890","name": "John Doe","iat": 1516239022},
            chave="your-256-bit-secret",
            algoritmo="HS256",
            header={}
        )
    
def testClassCriarDictionary():
    dictionary = {
        "payload" : {"sub": "1234567890","name": "John Doe","iat": 1516239022},
        "chave" : "your-256-bit-secret",
        "algoritmo" : "HS256",
        "header" : {"typ": "JWT"}
    }
    token = Token.fromDict(dictionary)
    assert token.payload == dictionary['payload']


    

    
