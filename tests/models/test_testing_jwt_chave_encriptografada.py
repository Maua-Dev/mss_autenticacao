from tests.models.test_model_jwt_chave_encriptografar import JWTChave
import pytest

def testClass():
    # Usando valores default de documentação pyjwt. rsa com senha.
    jWTChave = JWTChave(
        privateChave= b"-----BEGIN PRIVATE KEY-----\nMIGEAgEAMBAGByqGSM49AgEGBS...",
        senha= b"your password",
        )
    
    assert jWTChave.privateChave == "-----BEGIN PRIVATE KEY-----\nMIGEAgEAMBAGByqGSM49AgEGBS..."
    assert jWTChave.senha == "your password"

def testThrowExceptionFaltandoPrivateChave():
    with pytest.raises(Exception) as ValueError:
        jWTChave = JWTChave(
            privateChave= "",
            senha= b"your password",
        )
        
def testThrowExceptionFaltandoSenha():
    with pytest.raises(Exception) as ValueError:
        jWTChave = JWTChave(
            privateChave= b"-----BEGIN PRIVATE KEY-----\nMIGEAgEAMBAGByqGSM49AgEGBS...",
            senha= "",
        )

    
