from abc import ABC, abstractmethod


class BaseModel(ABC):
    @abstractmethod
    def printModel(self):
        pass
