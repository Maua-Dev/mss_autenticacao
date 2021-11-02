from src.controladores.fastapi.c_verificar_token_fastapi import CVerificarTokenFastAPI
from src.repositorios.jwt.auth_jwt import AuthJWT
from src.repositorios.oauth.auth_o_auth import AuthOAuth
from src.repositorios.otp.auth_otp import AuthOTP
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
    