from src.controladores.fastapi.c_gerar_token_fastapi import CGerarTokenFastAPI
from src.controladores.fastapi.c_verificar_token_fastapi import CVerificarTokenFastAPI

from src.interfaces.i_auth import IAuth


class FabricaControladorFastAPI:
    iauth : IAuth
    
    def __init__ (self, iauth: IAuth):
        self.iauth = iauth
        
    def gerarToken(self, body: dict):
        return CGerarTokenFastAPI(self.iauth)(body)
    
    def verificarToken(self, body: str):
        return CVerificarTokenFastAPI(self.iauth)(body)