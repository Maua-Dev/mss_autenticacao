from typing import List

from pydantic import BaseModel, validator, ValidationError
import re
from devmaua.src.enum.roles import Roles

from .erros.erros_models import ErroEmailInvalido
from .erros.erros_models import ErroEmailVazio
from .erros.erros_models import ErroSenhaVazio
from .erros.erros_models import ErroConversaoRequestLogin
from .erros.erros_models import ErroConversaoStrRole

class Login(BaseModel):
    email: str
    senha: str
    roles: list[Roles] = []

    @validator('senha')
    def senhaNaoVazia(cls, v):
        if len(v) == 0:
            raise ErroSenhaVazio
        return v

    @validator('email')
    def emailNaoVazio(cls, v):
        if len(v) == 0:
            raise ErroEmailVazio
        return v

    @validator('email')
    def emailValido(cls, v):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if not re.fullmatch(regex, v):
            raise ErroEmailInvalido
        return v


    @staticmethod
    def fromDict(d: dict):
        try:
            #TODO validar: talvez de so para deixar um **kargs e tirar esse metodo
            login = Login(
                email=d["email"],
                senha=d["senha"]
            )

            return login

        except(ErroEmailVazio, ErroEmailInvalido, ErroSenhaVazio) as e:
            raise e
        except:
            raise ErroConversaoRequestLogin

    def atualizarRoles(self, roles: list[Roles]):
        self.roles = roles

    @staticmethod
    def rolesFromStrList(roles: list[str]) -> List[Roles]:
        returnRoles = []
        try:
            for role in roles:
                returnRoles.append(Roles[role.upper()])
        except:
            raise ErroConversaoStrRole()
        return returnRoles
