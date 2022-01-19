import email
from src.repositorios.postgre.postgres_repository import PostgresRepository
from src.models.login import Login
from src.envs import Envs, EnvEnum


class Test_PostgresRepository:

    def test_login_with_db_local(self):
        repository = PostgresRepository()
        response = repository.emailExiste('15.01310-3@maua.br')
        assert response
    def test_login_fail_with_db_local(self):
        repository = PostgresRepository()
        response = repository.emailExiste('16.01310-3@maua.br')
        assert not response
        
    def test_register_with_db_local(self):
        login = Login(email="10.0000@0.maua", senha="10.0000@0.maua")
        repository = PostgresRepository()
        response = repository.cadastrarLoginAuth(login)
        assert response
    def test_register_fail_with_db_local(self):
        repository = PostgresRepository()
        response = repository.emailExiste('16.01310-3@maua.br')
        assert not response

    # def test_login_with_db_des(self):
    #     Envs.appEnv = EnvEnum.DES
    #     repository = PostgresRepository()
    #     response = repository.emailExiste('15.01310-3@maua.br')
    #     assert response
    # def test_login_fail_with_db_des(self):
    #     Envs.appEnv = EnvEnum.DES
    #     repository = PostgresRepository()
    #     response = repository.emailExiste('16.01310-3@maua.br')
    #     assert not response
