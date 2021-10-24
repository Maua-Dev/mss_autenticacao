from fastapi import APIRouter

from .rotas.rotas_mss_info import RotasMssInfo
from .rotas.rotas_login import RotasLogin
from .rotas.rotas_cadastrar import RotasCadastrar
from .rotas.rotas_atualiza import RotasAtualiza



class Roteador(APIRouter):

    def __init__(self, _ctrl):

        super().__init__()

        self.include_router(RotasMssInfo())
        self.include_router(RotasLogin(_ctrl))
        self.include_router(RotasCadastrar(_ctrl))
        self.include_router(RotasAtualiza(_ctrl))
