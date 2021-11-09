from fastapi import FastAPI


from src.controladores.fastapi.c_alterar_senha import CAlterarSenhaFastApi
from src.controladores.fastapi.c_esqueci_senha import CEsqueciSenhaFastAPI
from src.controladores.fastapi.c_gerar_token_fastapi import CGerarTokenFastAPI
from src.controladores.fastapi.c_verificar_token_fastapi import CVerificarTokenFastAPI
from src.controladores.fastapi.c_cadastrar_login_auth_fastapi import CCadastrarLoginAuthFastApi
from src.controladores.fastapi.c_logar_fastapi import CLogarFastApi
from src.controladores.fastapi.c_atualizar_roles import CAtualizarRolesFastApi

from src.interfaces.i_auth import IAuth
from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.interfaces.i_operacoes_hash import IOperacoesHash
from src.config.enums.fastapi import *
from src.config.proj_config import ProjConfig
from src.controladores.fastapi.roteadores.roteador import Roteador
from src.controladores.fastapi.start import Start


class FabricaControladorFastAPI:
    iauth: IAuth
    repo: IArmazenamento
    iHash: IOperacoesHash
    __config__: dict
    protocolo: str
    host: str
    porta: str
    root: str
    url: str

    app: FastAPI

    def __init__ (self, iauth: IAuth, repo: IArmazenamento, iHash: IOperacoesHash):
        self.iauth = iauth
        self.repo = repo
        self.iHash = iHash

        self.__config__ = ProjConfig.getFastapi()

        self.protocolo = self.__config__[KEY.PROTOCOLO.value]
        self.host = self.__config__[KEY.HOST.value]
        self.porta = self.__config__[KEY.PORTA.value]
        self.root = self.__config__[KEY.ROOT.value]
        self.url = f'{self.protocolo}://{self.host}:{self.porta}{self.root}'

        self.app = FastAPI()
        self.app.include_router(Roteador(self))
    
    def verificarToken(self, body: str):
        return CVerificarTokenFastAPI(self.iauth)(body)

    def cadastrarLogin(self, body: str):
        return CCadastrarLoginAuthFastApi(self.repo, self.iHash)(body)

    def logar(self, body: str):
        return CLogarFastApi(self.repo, self.iauth, self.iHash)(body)

    def atualizarRoles(self, body: str):
        return CAtualizarRolesFastApi(self.repo)(body)
    
    def esqueciSenha(self, body: dict):
        return CEsqueciSenhaFastAPI(self.repo, self.iauth)(body)
    
    def alterarSenha(self, body: dict):
        return CAlterarSenhaFastApi(self.repo, self.iauth, self.iHash)(body)

    def start(self):
        return Start()