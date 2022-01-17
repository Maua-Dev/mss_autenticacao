from cmath import log
from bcrypt import re
from devmaua.src.enum.roles import Roles

from src.interfaces.i_crud import ICRUD
from src.interfaces.i_crudfields import ICRUD_Fields
from src.models.login import Login
from src.models.conexao import Conexao

from src.repositorios.erros.erros_conexao import ErroFalhaConectar, ErroCriar, ErroEditar, ErroLer, ErroDeletar

import psycopg2

class CRUD_Postgre(ICRUD, ICRUD_Fields):

    def __init__(self):
        try:
            self.conexao = Conexao.fromEnv()
            self.conn = psycopg2.connect(
            host=self.conexao.host,
            database=self.conexao.database,
            user=self.conexao.usuario,
            password=self.conexao.senha
            )
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                                CREATE TABLE IF NOT EXISTS %s(
                                    id SERIAL PRIMARY KEY,
                                    email TEXT NOT NULL UNIQUE,
                                    senha TEXT NOT NULL,
                                    roles TEXT[][]
                                );
                                """, self.conexao.tabela)
            self.conn.commit()
            
        except Exception:
            print(Exception)
        
    
    def create(self, login:Login):
        try:
            self.cursor.execute("INSERT INTO " + self.getTableName() +"(email, senha) VALUES('%s', '%s') RETURNING id;", login.email, login.senha)
            if (self.cursor.fetchone()[0] != None):
                self.conn.commit()
                return True
            else:
                print ("Unknown error creating")
                return False
        except Exception:
            print (Exception)
            return False
    
    def update(self, login:Login):
        try:
            self.cursor.execute("UPDATE " + self.getTableName() + " SET senha = %s, roles = %s WHERE email = %s RETURNING id;", login.senha, login.roles, login.email)
            if (self.cursor.fetchone()[0] != None):
                self.conn.commit()
                return True
            else:
                print ("Unknown error updating")
                return False
        except Exception:
            print (Exception)
            return False
        
    def read(self, login:Login):
        try:
            self.cursor.execute("SELECT * FROM " + self.getTableName)
            logins = self.cursor.fetchall
            if (len(logins) == 0):
                self.conn.commit()
                return logins
            else:
                print ("Unknown error reading")
                return False
        except Exception:
            print (Exception)
            return False
    
    def readByEmail(self, login:Login):
        try:
            self.cursor.execute("SELECT * FROM " + self.getTableName + " WHERE email = %s;", login.email)
            logins = self.cursor.fetchall
            if (len(logins) == 0):
                self.conn.commit()
                return logins
            else:
                print ("Unknown error reading")
                return False
        except Exception:
            print (Exception)
            return False


    def delete(self, login:Login):
        try:
            self.cursor.execute("DELETE FROM " + self.getTableName() + " WHERE email = %s RETURNING id;", login.email)
            if (self.cursor.fetchone()[0] != None):
                self.conn.commit()
                return True
            else:
                print ("Error deleting")
                return False
        except Exception:
            print (Exception)
            return False
    
    def getTableName(self):
        return self.conexao.tabela

    def getDeleteString(self):
        pass

    def getUpdateString(self):
        pass

    def getInsertString(self):
        return "INSERT INTO " + self.getTableName() +"(email, senha) VALUES(%s, %s)"

    def getSelectAllString(self):
        pass

    def getSelectConditionalString(self):
        pass