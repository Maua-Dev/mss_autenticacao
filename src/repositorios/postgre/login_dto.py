
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship

from src.models.login import Login
from src.repositorios.postgre.db_base import Base



class LoginDto(Base):
    __tablename__ = 'Login'

    id = Column(Integer, primary_key=True, nullable=False)
    id_fk = Column(Integer, ForeignKey("User.id"))
    senha= Column(String, nullable=False)

    # 1-1 -- login - user
    user_back = relationship("User")#, back_populates="Login")