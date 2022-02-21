
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship

from src.models.login import Login
from devmaua.src.enum.roles import Roles
from src.repositorios.postgre.db_base import Base



class RoleDto(Base):
    __tablename__ = 'Role'

    id = Column(Integer, primary_key=True)
    id_fk = Column(Integer, ForeignKey("User.id"))
    role = Column(Integer, nullable=False, unique=True)
          
    # N-1 -- Role - User
    user_back = relationship("UserDto", back_populates="Role")