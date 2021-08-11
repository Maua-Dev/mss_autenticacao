import jwt
import pathlib
import os
from dotenv import dotenv_values

from src.interfaces.i_jwt_encriptografar import IJWTEncriptografar
from src.models.m_jwt_token import JWTToken

class UCCriarJWT():

    iJWTEncriptografar : IJWTEncriptografar
    
    def __init__(self, iJWTEncriptografar : IJWTEncriptografar):
        self.iJWTEncriptografar = iJWTEncriptografar
        
    def criarJWT(self, modelJWTToken: JWTToken):
        try:
            config = dotenv_values(".env")
            print("Before loading file")
            print("After loading file")
            encoded = jwt.encode(modelJWTToken.payload, config["password"], algorithm="HS256", headers={"typ": "JWT"})
            return encoded
        except:
            raise Exception