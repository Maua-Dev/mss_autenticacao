from fastapi import APIRouter

from .rotas.rotas_mss_info import RotasMssInfo



class Roteador(APIRouter):

    def __init__(self, _ctrl):

        super().__init__()

        self.include_router(RotasMssInfo())