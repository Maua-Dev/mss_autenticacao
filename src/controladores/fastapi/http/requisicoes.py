
from typing import Optional

from pydantic import BaseModel


class ReqExemplo(BaseModel):
    arg: Optional[str]
    
class ModeloEsqueciSenha(BaseModel):
    email: str
    
class ModeloAlterarSenha(BaseModel):
    token: str
    email: str
    novasenha: str