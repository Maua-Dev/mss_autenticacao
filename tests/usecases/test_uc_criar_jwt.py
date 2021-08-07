from src.usecases.uc_criar_jwt import UCCriarJWT
import pytest
@pytest.mark.xfail
def testeFailCriarCasePayloadVazio():
    ucCriarJWT = UCCriarJWT().criarToken({},"secret","HS256")
    if not ucCriarJWT:
        assert False
    else:
        assert True
 
@pytest.mark.xfail       
def testeFailCriarCaseSecretVazio():
    ucCriarJWT = UCCriarJWT().criarToken({"sub": "1234567890","name": "John Doe","iat": 1516239022},"","HS256")
    if not ucCriarJWT:
        assert False
    else:
        assert True
     
@pytest.mark.xfail   
def testeFailCriarCaseAlgoritmoVazio():
    ucCriarJWT = UCCriarJWT().criarToken({"sub": "1234567890","name": "John Doe","iat": 1516239022},"secret","")
    if not ucCriarJWT:
        assert False
    else:
        assert True

@pytest.mark.xfail
def testeFailCriarCaseTudoVazio():
    ucCriarJWT = UCCriarJWT().criarToken({},"","")
    if not ucCriarJWT:
        assert False
    else:
        assert True