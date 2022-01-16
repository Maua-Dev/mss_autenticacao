import abc
from logging import exception
from pydantic import BaseModel, validator, ValidationError
from dotenv import dotenv_values


class Conexao(BaseModel):
    host: str
    database: str
    tabela: str
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
    
    @validator('tabela')
    def tabelaNaoVazia(cls, v):
        if len(v) == 0:
            raise ValueError("Tabela Vazia")
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

    @staticmethod
    def fromEnv():
        try:
            chave = dotenv_values(".env")
            conn = Conexao(
                host = chave["host_sql"],
                database = chave["database_sql"],
                tabela = chave["table_sql"],
                usuario = chave["user_sql"],
                senha = chave["password_sql"]
            )
            return conn
        except:
            raise exception
        