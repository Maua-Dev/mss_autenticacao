
from sqlalchemy import Column, Integer, String, Sequence

from src.models.login import Login
from devmaua.src.enum.roles import Roles
from src.repositorios.postgre.db_base import Base



class RoleDto(Base):
    __tablename__ = 'Role'

    id = Column(Integer, primary_key=True)
    role = Column(String, nullable=False, unique=True)
    
          