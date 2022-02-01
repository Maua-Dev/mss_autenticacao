from enum import Enum
import os
class Config():
    sqlConnection: str

class ConfigLocal(Config):
    def __init__(self) -> None:
        super().__init__()
        self.sqlConnection = f'postgresql://postgres:devmaua@{os.getenv("DB") or "localhost"}:5432/Devmaua'
class ConfigDes(Config):
    def __init__(self) -> None:
        super().__init__()
        self.sqlConnection = f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PW")}@db-devmaua-identifier.cjzimvmkm7zt.sa-east-1.rds.amazonaws.com:5432/{os.getenv("DB_NAME")}'
class ConfigProd(Config):
    def __init__(self) -> None:
        super().__init__()
        self.sqlConnection = ''


class EnvEnum(Enum):
    LOCAL = 'Local'
    DES = 'Development'    
    PROD = 'Production'


class Envs:
    appEnv: EnvEnum = EnvEnum(os.getenv('PYTHON_ENV') or 'Local')
    @staticmethod
    def IsLocal():
        return Envs.appEnv == EnvEnum.LOCAL
    
    @staticmethod
    def IsDes():
        return Envs.appEnv == EnvEnum.DES
    
    @staticmethod    
    def IsProd():
        return Envs.appEnv == EnvEnum.PROD

    @staticmethod    
    def getConfig() -> Config:        
        if(Envs.IsLocal()):
            return ConfigLocal()
        if(Envs.IsDes()):
            return ConfigDes()
        if(Envs.IsProd()):
            return ConfigProd()
        return ConfigLocal()