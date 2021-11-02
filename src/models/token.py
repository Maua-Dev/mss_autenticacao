import abc
from pydantic import BaseModel, validator, ValidationError


class Token(BaseModel):
    payload: dict
    chave: str
    algoritmo: str
    header: dict
    
    @validator('payload', check_fields=False)
    def payloadNaoVazio(cls, v):
        if len(v) == 0:
            raise ValueError("Payload Vazio")
        return v
    
    @validator('chave')
    def chaveNaoVazia(cls, v):
        if len(v) == 0:
            raise ValueError("Chave Vazia")
        return v
        
    @validator('algoritmo')
    def algoritmoNaoVazio(cls, v):
        if len(v) == 0:
            raise ValueError("Algoritmo Vazio")
        return v
        
    @validator('header', check_fields=False)
    def headerNaoVazio(cls, v):
        if len(v) == 0:
            raise ValueError("Header Vazio")
        return v
    
    @staticmethod
    def fromDict(d: dict):
        try:
            token = Token(
                payload = d['payload'],
                chave = "your-256-bit-secret",
                algoritmo = "HS256",
                header = {"kid": "230498151c214b788dd97f22b85410a5"}
            )
            return token
        except:
            raise Exception
