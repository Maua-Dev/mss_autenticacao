from abc import ABC, abstractmethod

class ICRUD_Fields(ABC):
    @abstractmethod
    def getTableName(self):
        pass

    @abstractmethod
    def getDeleteString(self):
        pass

    @abstractmethod
    def getUpdateString(self):
        pass

    @abstractmethod
    def getInsertString(self):
        pass

    @abstractmethod
    def getSelectAllString(self):
        pass

    @abstractmethod
    def getSelectConditionalString(self):
        pass