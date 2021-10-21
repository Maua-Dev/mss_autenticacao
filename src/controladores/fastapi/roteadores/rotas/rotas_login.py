from fastapi import APIRouter, Request


class RotasLogin(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/rota1", responses={404: {"description": "Not found"}})

        @self.post("/login")
        async def logar(request: Request):
            return _ctrl.logar(await request.json())
