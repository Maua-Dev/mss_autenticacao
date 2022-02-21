
from sqlalchemy import Column, Integer, String, Sequence, ARRAY, ForeignKey
from sqlalchemy.orm import relationship

from src.models.login import Login
from src.repositorios.postgre.db_base import Base



class UsersDto(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    email= Column(String, nullable=False, unique=True)
    
    # 1-1 -- user - login
    login_back = relationship("LoginDto", back_populates="User", uselist=False)
    
    # 1-n -- user - role
    role_back = relationship("RoleDto", back_populates="User")