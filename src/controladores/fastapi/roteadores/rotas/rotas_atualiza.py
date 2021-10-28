from fastapi import APIRouter, Request


class RotasAtualiza(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/atualiza", responses={404: {"description": "Not found"}})

        @self.post("/roles")
        async def atualizarRoles(request: Request):
            return _ctrl.atualizarRoles(await request.json())
