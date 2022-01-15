import abc
from pydantic import BaseModel, validator, ValidationError
from dotenv import dotenv_values


class Conexao(BaseModel):
    host: str
    database: str
    usuario: str
    senha: str
    
    @validator('host', check_fields=False)
    def hostNaoVazio(cls, v):
        if len(v) == 0:
            raise ValueError("Host Vazio")
        return v
    
    @validator('database')
    def databaseNaoVazio(cls, v):
        if len(v) == 0:
            raise ValueError("Database Vazio")
        return v

    @validator('usuario')
    def usuarioNaoVazio(cls, v):
        if len(v) == 0:
            raise ValueError("Usuario Vazio")
        return v

    @validator('senha')
    def senhaNaoVazia(cls, v):
        if len(v) == 0:
            raise ValueError("Senha Vazio")
        return v
