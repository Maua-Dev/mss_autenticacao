from src.config.proj_config import ProjConfig
from src.config.erros.deployment import *
from src.config.enums.deployment import *
from src.repositorios.jwt.auth_jwt import AuthJWT
from src.repositorios.volatil.armazenamento_volatil import ArmazenamentoUsuarioVolatil
from src.fabricas.controladores.fastapi.fabrica_controlador_fastapi import FabricaControladorFastAPI
from src.controladores.hashing.bcrypt.c_operacoes_bcrypt import COperacoesBcrypt


class Init:
    def __call__(
            self,
            tipo_repo: str = ProjConfig.getDeployment()[KEY.TIPO_REPOSITORIO.value],
            tipo_ctrl: str = ProjConfig.getDeployment()[KEY.TIPO_CONTROLADOR.value]
    ):
        # Instanciando tipo de REPOSITORIO
        if tipo_repo == REPOSITORIO.MOCK.value:
            repo = ArmazenamentoUsuarioVolatil()
        else:
            raise ErroDeployment1()

        # Instanciando tipo de CONTROLER
        if tipo_ctrl == CONTROLADOR.FASTAPI.value:
            ctrl = FabricaControladorFastAPI(AuthJWT(), repo, COperacoesBcrypt)
        else:
            raise ErroDeployment2()

        return repo, ctrl
