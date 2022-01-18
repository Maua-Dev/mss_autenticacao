from src.repositorios.postgre.postgres_repository import PostgresRepository
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
