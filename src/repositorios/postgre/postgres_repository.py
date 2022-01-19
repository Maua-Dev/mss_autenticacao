import email
from unicodedata import name
from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login
from src.repositorios.postgre.db_config import DBConnectionHandler
from src.repositorios.postgre.login_dto import LoginDto
from devmaua.src.enum.roles import Roles

class PostgresRepository(IArmazenamento):

    def emailExiste(self, email: str):
        with DBConnectionHandler() as db:
            try:
                response = db.session.query(LoginDto).filter(LoginDto.email == email).first()
                if(response):
                    return True
                else:
                    return False
            except Exception  as error:
                print(error)
                return False

    def cadastrarLoginAuth(self, login: Login):
        with DBConnectionHandler() as db:
            try:
                response = db.session.insert(LoginDto).values(email=login.email, senha=login.senha).returning(id)
                if(response >= 0):
                    return True
                else:
                    return False
            except Exception  as error:
                print(error)
                return False

    
    def alterarSenha(self, login: Login):
        pass

    
    def deletarLoginAuthPorEmail(self, email: str):
        pass

    
    def getSenhaEncriptadaPorEmail(self, email: str):
        pass

    
    def atualizarRolePorEmail(self, email: str, roles: list[Roles]):
        pass

    
    def getRolesPorEmail(self, email: str):
        pass