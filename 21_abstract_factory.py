'''
Creational Design Patterns
Provides an interface for creating families of related objects.
'''

from abc import ABC, abstractmethod

class AbstractFactory:
    @abstractmethod
    def createProductA():
        pass
    @abstractmethod
    def createProductB():
        pass

class ConcreteFactory1(AbstractFactory):
    def __init__(self) -> None:
        super().__init__()

    def createProductA(self):
        pass

    def createProductB(self):
        pass

class ConcreteFactory2(AbstractFactory):
    def __init__(self) -> None:
        super().__init__()

    def createProductA(self):
        pass

    def createProductB(self):
        pass