'''
Creational Design Patterns
To create new objects by copying an existing object.
'''

from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone():
        pass

class ConcretePrototype(Prototype):
    def __init__(self) -> None:
        super().__init__()
    
    def clone():
        pass

class Client:
    def __init__(self,prototype) -> None:
        self.prototype = prototype
    
    