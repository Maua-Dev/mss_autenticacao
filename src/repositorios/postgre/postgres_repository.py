from cmath import log
from distutils.log import Log
import email
import psycopg2
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
                logger = LoginDto(email=login.email, senha=login.senha)
                response = db.session.add(logger)
                response = db.session.commit()
                if(self.emailExiste(email=logger.email)):
                    return True
                else:
                    return False
            except Exception  as error:
                print(error)
                return False

    
    def alterarSenha(self, login: Login):
        with DBConnectionHandler() as db:
            try:
                #logger = LoginDto(email=login.email, senha=login.senha)
                response = db.session.query(LoginDto).filter(LoginDto.email == login.email).first()
                response.senha = login.senha
                response = db.session.commit()
                if(self.getSenhaEncriptadaPorEmail(login.email) == login.senha):
                    return True
                else:
                    return False
            except Exception  as error:
                print(error)
                return False

    
    def deletarLoginAuthPorEmail(self, email: str):
        with DBConnectionHandler() as db:
            try:
                response = db.session.query(LoginDto).filter(LoginDto.email == email).delete()
                response = db.session.commit()
                if(not self.emailExiste(email=email)):
                    return True
                else:
                    return False
            except Exception  as error:
                print(error)
                return False
    
    def getSenhaEncriptadaPorEmail(self, email: str):
        with DBConnectionHandler() as db:
            try:
                response = db.session.query(LoginDto).filter(LoginDto.email == email).first()
                if(response):
                    return response.senha
                else:
                    return ""
            except Exception  as error:
                print(error)
                return ""

    
    def atualizarRolePorEmail(self, email: str, roles: list[Roles]):
        pass

    
    def getRolesPorEmail(self, email: str):
        pass