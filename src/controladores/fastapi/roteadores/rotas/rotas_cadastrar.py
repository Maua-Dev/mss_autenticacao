from fastapi import APIRouter, Request


class RotasCadastrar(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/cadastrar", responses={404: {"description": "Not found"}})

        @self.post("")
        async def cadastrarLogin(request: Request):
            return _ctrl.cadastrarLogin(await request.json())
