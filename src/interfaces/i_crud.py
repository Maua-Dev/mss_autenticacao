from abc import ABC, abstractmethod
from src.models.login import Login

class ICRUD(ABC):

    @abstractmethod
    def create(self, login:Login):
        pass
    
    @abstractmethod
    def update(self, login:Login):
        pass

    @abstractmethod
    def read(self, login:Login):
        pass

    @abstractmethod
    def delete(self, login:Login):
        pass
