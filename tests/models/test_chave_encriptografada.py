from src.models.chave import Chave
import pytest

def testClass():
    # Usando valores default de documentação pyjwt. rsa com senha.
    chave = Chave(
    
        chavePrivada= b"-----BEGIN PRIVATE KEY-----\nMIGEAgEAMBAGByqGSM49AgEGBS...",
        senha= b"your password",
        )
    
    assert chave.chavePrivada == "-----BEGIN PRIVATE KEY-----\nMIGEAgEAMBAGByqGSM49AgEGBS..."
    assert chave.senha == "your password"

def testExceptionFaltandoChavePrivada():
    with pytest.raises(Exception) as ValueError:
        chave = Chave(
            chavePrivada= "",
            senha= b"your password",
        )
        
def testExceptionFaltandoSenha():
    with pytest.raises(Exception) as ValueError:
        chave = Chave(
            chavePrivada= b"-----BEGIN PRIVATE KEY-----\nMIGEAgEAMBAGByqGSM49AgEGBS...",
            senha= "",
        )

    
