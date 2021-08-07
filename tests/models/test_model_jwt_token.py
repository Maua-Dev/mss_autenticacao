import abc
from pydantic import BaseModel, validator, ValidationError

import jwt

class JWTToken(BaseModel):
    payload : dict
    chave : str
    algoritmo : str
    header : dict
    
    @validator('payload', check_fields=False)
    def payloadNotEmpty(cls, v):
        if (len(v) == 0):
            raise ValueError("Payload Vazio")
        return v
    
    @validator('chave')
    def chaveNotEmpty(cls, v):
        if (len(v) == 0):
            raise ValueError("Chave Vazio")
        return v
        
    @validator('algoritmo')
    def algoritmoNotEmpty(cls, v):
        if (len(v) == 0):
            raise ValueError("Algoritmo Vazio")
        return v
        
    @validator('header', check_fields=False)
    def headerNotEmpty(cls, v):
        if (len(v) == 0):
            raise ValueError("Header Vazio")
        return v
    
        

    
    