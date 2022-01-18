from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.envs import Envs

from src.repositorios.postgre.db_base import Base


class DBConnectionHandler:
    # session: Optional[sessionmaker]
    def __init__(self):
        self.__connection_string = Envs.getConfig().sqlConnection
        self.session: Optional[sessionmaker] = None

    def get_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):        
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        Base.metadata.create_all(engine)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):   
        if(isinstance(self.session,sessionmaker)):
            self.session.close() # pylint: disable=no-member