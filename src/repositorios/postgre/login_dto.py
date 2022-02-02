
from sqlalchemy import Column, Integer, String, Sequence

from src.models.login import Login
from src.repositorios.postgre.db_base import Base



class LoginDto(Base):
    __tablename__ = 'Login'

    id = Column(Integer, primary_key=True)
    email= Column(String, nullable=False, unique=True)
    senha= Column(String, nullable=False)
    

    def toEntity(self) -> Login:
        return Login(
            email=self.email,
            senha=self.senha
        )        