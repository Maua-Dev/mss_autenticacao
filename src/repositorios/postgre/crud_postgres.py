from devmaua.src.enum.roles import Roles

from src.interfaces.i_crud import ICRUD
from src.interfaces.i_crudfields import ICRUD_Fields
from src.models.login import Login
from src.models.conexao import Conexao

from src.repositorios.erros.erros_conexao import ErroFalhaConectar, ErroCriar, ErroEditar, ErroLer, ErroDeletar

class CRUD_Postgre(ICRUD, ICRUD_Fields):

    def __init__(self):
        self.conexao = Conexao.fromEnv()