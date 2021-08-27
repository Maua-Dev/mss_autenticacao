from pydantic import BaseModel, validator, ValidationError
import re


class Login(BaseModel):
    email: str
    senhaEncriptada: str

    @validator('senhaEncriptada')
    def senhaNaoVazia(cls, v):
        if len(v) == 0:
            raise ValueError("Senha Vazia")
        return v

    @validator('email')
    def emailNaoVazio(cls, v):
        if len(v) == 0:
            raise ValueError("Email Vazio")
        return v

    @validator('email')
    def emailValido(cls, v):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if not re.fullmatch(regex, v):
            raise ValueError("Email Invalido")
        return v
