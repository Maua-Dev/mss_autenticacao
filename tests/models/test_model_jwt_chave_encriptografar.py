import abc
from pydantic import BaseModel, validator, ValidationError

class JWTChave(BaseModel):
    privateChave : str
    senha : str
    
    @validator('privateChave', check_fields=False)
    def privateChaveNotEmpty(cls, v):
        if (len(v) == 0):
            raise ValueError("PrivateChave Vazio")
        return v
    
    @validator('senha')
    def senhaNotEmpty(cls, v):
        if (len(v) == 0):
            raise ValueError("Senha Vazio")
        return v
        
    
        

    
    