from fastapi import APIRouter

from .rotas.rotas_mss_info import RotasMssInfo
from .rotas.rotas_login import RotasLogin
from .rotas.rotas_cadastrar import RotasCadastrar
from .rotas.rotas_atualiza import RotasAtualiza
from .rotas.rotas_validar import RotasValidar
from .rotas.rotas_esqueci_senha import RotasEsqueciSenha
from .rotas.rotas_alterar_senha import RotasAlterarSenha



class Roteador(APIRouter):

    def __init__(self, _ctrl):

        super().__init__()

        self.include_router(RotasMssInfo())
        self.include_router(RotasLogin(_ctrl))
        self.include_router(RotasCadastrar(_ctrl))
        self.include_router(RotasAtualiza(_ctrl))
        self.include_router(RotasValidar(_ctrl))
        self.include_router(RotasEsqueciSenha(_ctrl))
        self.include_router(RotasAlterarSenha(_ctrl))
