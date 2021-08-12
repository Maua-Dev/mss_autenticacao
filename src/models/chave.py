import abc
from pydantic import BaseModel, validator, ValidationError

class Chave(BaseModel):
    chavePrivada : str
    senha : str
    
    @validator('chavePrivada', check_fields=False)
    def chavePrivadaNaoVazia(cls, v):
        if (len(v) == 0):
            raise ValueError("chavePrivada Vazio")
        return v
    
    @validator('senha')
    def senhaNaoVazia(cls, v):
        if (len(v) == 0):
            raise ValueError("Senha Vazio")
        return v
        
    
        

    
    