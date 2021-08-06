from src.usecases.uc_criar_jwt import UCCriarJWT
import pytest
def testeCriarCasePayloadVazio():
    ucCriarJWT = UCCriarJWT({},"secret","HS256")
    if not ucCriarJWT:
        assert False
    else:
        assert True
        
def testeCriarCaseSecretVazio():
    ucCriarJWT = UCCriarJWT({"sub": "1234567890","name": "John Doe","iat": 1516239022},"","HS256")
    if not ucCriarJWT:
        assert False
    else:
        assert True
        
def testeCriarCaseAlgoritmoVazio():
    ucCriarJWT = UCCriarJWT({"sub": "1234567890","name": "John Doe","iat": 1516239022},"secret","")
    if not ucCriarJWT:
        assert False
    else:
        assert True