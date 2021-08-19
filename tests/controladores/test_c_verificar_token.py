from src.controladores.c_verificar_token import CVerificarToken
from src.repositorios.jwt.authJWT import AuthJWT
from src.repositorios.oauth.authOAuth import AuthOAuth
from src.repositorios.otp.authOTP import AuthOTP
import pytest

@pytest.mark.skip
def testDecodeJWT():
    controllerVerificarToken = CVerificarToken(AuthJWT())
    controllerVerificarToken('REPLACEMEWITHATOKEN')
    assert True
    