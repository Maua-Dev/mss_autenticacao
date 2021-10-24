from fastapi import APIRouter, Request


class RotasValidar(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/validar", responses={404: {"description": "Not found"}})

        @self.get("")
        async def atualizarRoles(request: Request):
            token = request.headers['Authorization'].split()[1]
            return _ctrl.verificarToken(token)
