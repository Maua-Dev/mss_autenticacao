from enum import Enum

class Config():
    sqlConnection: str

class ConfigLocal(Config):
    def __init__(self) -> None:
        super().__init__()
        self.sqlConnection = 'postgresql://postgres:devmaua@localhost:5432/Dev.Materias'
class ConfigDes(Config):
    def __init__(self) -> None:
        super().__init__()
        self.sqlConnection = 'postgresql://postgres:DevMaua2022!@db-devmaua-identifier.cjzimvmkm7zt.sa-east-1.rds.amazonaws.com:5432/DevMaua_DB_dev'
class ConfigProd(Config):
    def __init__(self) -> None:
        super().__init__()
        self.sqlConnection = ''


class EnvEnum(Enum):
    LOCAL = 'Local'
    DES = 'Development'    
    PROD = 'Production'


class Envs:
    appEnv: EnvEnum = EnvEnum.LOCAL

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