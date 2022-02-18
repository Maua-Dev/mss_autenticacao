
from sqlalchemy import Column, Integer, String, Sequence, ARRAY

from src.models.login import Login
from src.repositorios.postgre.db_base import Base



class LoginDto(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    email= Column(String, nullable=False, unique=True)
    roles= Column(ARRAY(Integer))
    