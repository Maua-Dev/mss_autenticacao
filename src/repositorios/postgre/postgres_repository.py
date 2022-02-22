from cmath import log
from distutils.log import Log
import email
import psycopg2
from unicodedata import name
from src.interfaces.i_armazenamento_auth import IArmazenamento
from src.models.login import Login
from src.repositorios.postgre.db_config import DBConnectionHandler
from src.repositorios.postgre.users_dto import UsersDto
from src.repositorios.postgre.login_dto import LoginDto
from src.repositorios.postgre.role_dto import RoleDto


from devmaua.src.enum.roles import Roles

class PostgresRepository(IArmazenamento):

    def emailExiste(self, email: str):
        with DBConnectionHandler() as db:
            try:
                response = db.session.query(UsersDto).filter(UsersDto.email == email).first()
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
                user = UsersDto(email=login.email)
                
                response = db.session.add(user)
                response = db.session.commit()
                response = db.session.refresh(user)
                response = db.session.add(LoginDto(id_fk = response.id, senha=login.senha))
                response = self.atualizarRolePorEmail(email=login.email, roles=login.roles)
                response = db.session.commit()
                
                if(self.emailExiste(email=login.email)):
                    return True
                else:
                    return False
            except Exception  as error:
                print(error)
                return False

    
    def alterarSenha(self, login: Login):
        with DBConnectionHandler() as db:
            try:
                response = db.session.query(UsersDto).filter(UsersDto.email == login.email).first()
                response = db.session.query(LoginDto).filter(LoginDto.id_fk == response.id).first()
                response.senha = login.senha
                response = db.session.commit()

                if(self.getSenhaEncriptadaPorEmail(email=login.email)):
                    return True
                else:
                    return False

            except Exception as error:
                print(error)
                return False

    
    def deletarLoginAuthPorEmail(self, email: str):
        with DBConnectionHandler() as db:
            try:
                response = db.session.query(UsersDto).filter(UsersDto.email == email).first()
                response = db.session.delete(response)
                db.session.commit()
                if(not self.emailExiste(email=email)):
                    return True
                else:
                    return False
            except Exception as error:
                print(error)
                return False
    
    def getSenhaEncriptadaPorEmail(self, email: str):
        with DBConnectionHandler() as db:
            try:
                response = db.session.query(UsersDto).filter(UsersDto.email == email).first()
                response = db.session.query(LoginDto).filter(LoginDto.id_fk == response.id).first()
                
                if (response):
                    return response.senha
                else:
                    return ""

            except Exception as error:
                print(error)
                return ""

    
    def atualizarRolePorEmail(self, email: str, roles: list[Roles]):
        with DBConnectionHandler() as db:
            try:
                response = db.session.query(UsersDto).filter(UsersDto.email == email).first()
                fkey = response.id
                for role in roles:
                    db.session.add(RoleDto(id_fk=fkey, role=role.value))
                db.session.commit()
                return True

            except Exception as error:
                print(error)
                return False

    
    def getRolesPorEmail(self, email: str):
        with DBConnectionHandler() as db:
            try:
                response = db.session.query(UsersDto).filter(UsersDto.email == email).first()
                response = db.session.query(RoleDto).filter(RoleDto.id_fk).all()
                print(response)
                return response
            except Exception as error:
                print(error)
                return ""