from typing import Any, Optional

from pydantic import BaseModel


class ResPadrao(BaseModel):
    msg: str = 'Resposta padrão'


class ResRoot(BaseModel):
    deployment: dict
    controlador: dict


class ResArg(BaseModel):
    arg: Optional[Any]
    msg: Optional[str] = 'Resposta padrão'