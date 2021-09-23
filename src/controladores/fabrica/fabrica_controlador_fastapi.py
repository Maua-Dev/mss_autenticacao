from src.controladores.fastapi.c_gerar_token_fastapi import CGerarTokenFastAPI
from src.controladores.fastapi.c_verificar_token_fastapi import CVerificarTokenFastAPI
from src.controladores.fastapi.c_cadastrar_login_auth_fastapi import CCadastrarLoginAuthFastApi
from src.controladores.fastapi.c_logar_fastapi import CLogarFastApi
from src.controladores.fastapi.c_atualizar_roles import CAtualizarRolesFastApi

from src.interfaces.i_auth import IAuth
from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.interfaces.i_operacoes_hash import IOperacoesHash


class FabricaControladorFastAPI:
    iauth: IAuth
    repo: IArmazenamento
    iHash: IOperacoesHash
    
    def __init__ (self, iauth: IAuth, repo: IArmazenamento, iHash: IOperacoesHash):
        self.iauth = iauth
        self.repo = repo
        self.iHash = iHash
        
    def gerarToken(self, body: dict):
        return CGerarTokenFastAPI(self.iauth)(body)
    
    def verificarToken(self, body: str):
        return CVerificarTokenFastAPI(self.iauth)(body)

    def cadastrarLogin(self, body: str):
        return CCadastrarLoginAuthFastApi(self.repo, self.iHash)(body)

    def logar(self, body: str):
        return CLogarFastApi(self.repo, self.iauth, self.iHash)(body)

    def atualizarRoles(self, body: str):
        return CAtualizarRolesFastApi(self.repo)(body)
