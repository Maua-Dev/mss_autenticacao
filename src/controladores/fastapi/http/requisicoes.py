from typing import Optional

from pydantic import BaseModel


class ReqExemplo(BaseModel):
    arg: Optional[str]
    
class EsqueciSenha(BaseModel):
    email: str
    
class AlterarSenha(BaseModel):
    token: str
    email: str
    novasenha: str