from fastapi import APIRouter, Request


class RotasEsqueciSenha(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/esquecisenha", responses={404: {"description": "Not found"}})

        @self.post("")
        async def esqueciSenha(request: Request):
            return _ctrl.esqueciSenha(await request.json())
