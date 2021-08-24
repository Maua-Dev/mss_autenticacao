from src.controladores.fastapi.c_verificar_token_fastapi import CVerificarTokenFastAPI
from src.repositorios.jwt.authJWT import AuthJWT
from src.repositorios.oauth.authOAuth import AuthOAuth
from src.repositorios.otp.authOTP import AuthOTP
import pytest

@pytest.mark.skip
def testDecodeJWT():
    controllerVerificarToken = CVerificarTokenFastAPI(AuthJWT())
    controllerVerificarToken('REPLACEMEWITHATOKEN')
    assert True
    
@pytest.mark.skip
def testDecodeJWTError():
    controllerVerificarToken = CVerificarTokenFastAPI(AuthJWT())
    controllerVerificarToken('REPLACEMEWITHATOKEN')
    assert True
    