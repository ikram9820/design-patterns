'''
Creational Design Patterns
Allows separating the construction of an objects from its representation 
so the same construction algorithm can be applied to different representatons.
'''
from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def buildPaert():
        pass

class ConcreteBuilder(Builder):
    def __init__(self) -> None:
        super().__init__()

    def buildPaert(self):
        pass

    def getResult(self):
        pass

class Director:
    def __init__(self) -> None:
        pass

    def construct(self):
        builder = Builder()