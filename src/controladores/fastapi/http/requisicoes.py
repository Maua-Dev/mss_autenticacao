from typing import Optional

from pydantic import BaseModel


class ReqExemplo(BaseModel):
    arg: Optional[str]
