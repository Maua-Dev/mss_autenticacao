from src.usecases.uc_criar_token import UCCriarToken
from src.controladores.fastapi.c_gerar_token_fastapi import CGerarTokenFastAPI
from src.interfaces.i_auth import IAuth
from src.repositorios.jwt.auth_jwt import AuthJWT
from src.repositorios.oauth.auth_o_auth import AuthOAuth
from src.repositorios.otp.auth_otp import AuthOTP
import pytest

def testeGerarTokenAuthJWT():
    controllerGerarToken = CGerarTokenFastAPI(AuthJWT())
    controllerGerarToken({"payload" : {"test": "data"}})
    assert True
    
def testeGerarTokenAuthOAuth():
    controllerGerarToken = CGerarTokenFastAPI(AuthOAuth())
    controllerGerarToken({"payload" : {"test": "data"}})
    assert True
    
def testeGerarTokenAuthOTP():
    controllerGerarToken = CGerarTokenFastAPI(AuthOTP())
    controllerGerarToken({"payload" : {"test": "data"}})
    assert True
    