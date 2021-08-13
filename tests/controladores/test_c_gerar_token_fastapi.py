from src.usecases.uc_criar_token import UCCriarToken
from src.main import gerarToken
from src.controladores.c_gerar_token_fastapi import CGerarTokenFastAPI
from src.interfaces.i_auth import IAuth
from src.repositorios.jwt.authJWT import AuthJWT
from src.repositorios.oauth.authOAuth import AuthOAuth
from src.repositorios.otp.authOTP import AuthOTP
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
    