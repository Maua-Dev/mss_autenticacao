from fastapi import APIRouter, Request


class RotasAlterarSenha(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/alterarsenha", responses={404: {"description": "Not found"}})

        @self.post("")
        async def alterarSenha(request: Request):
            return _ctrl.alterarSenha(await request.json())
