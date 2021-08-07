import abc
from pydantic import BaseModel, validator, ValidationError

import jwt

class JWTToken(BaseModel):
    
    #@validator('payload', check_fields=False)
    #def payloadNotEmpty(cls, v):
    #    if (len(v) == 0):
    #        raise ValueError("Payload Vazio")
    
    #@validator('chave')
    #def chaveNotEmpty(cls, v):
    #    if (len(v) == 0):
    #        raise ValueError("Chave Vazio")
        
    #@validator('algoritmo')
    #def algoritmoNotEmpty(cls, v):
    #    if (len(v) == 0):
    #        raise ValueError("Algoritmo Vazio")
        
    #@validator('header', check_fields=False)
    #def headerNotEmpty(cls, v):
    #    if (len(v) == 0):
    #        raise ValueError("Header Vazio")
        
    def criarToken(self, payload : dict, chave : str, algoritmo : str, header : dict ):
        if (len(payload) == 0):
            raise ValueError("Payload Vazio")
        
        if (len(chave) == 0):
            raise ValueError("Chave Vazio")
        
        if (len(algoritmo) == 0):
            raise ValueError("Algoritmo Vazio")
        
        if (len(header) == 0):
            raise ValueError("Header Vazio")
        
        try:
            encoded = jwt.encode(payload, chave, algoritmo, header)
            return encoded
        except:
            return Exception
        
        

    
    