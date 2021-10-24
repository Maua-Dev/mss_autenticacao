from fastapi import APIRouter, Request


class RotasLogin(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/login", responses={404: {"description": "Not found"}})

        @self.post("")
        async def logar(request: Request):
            return _ctrl.logar(await request.json())
