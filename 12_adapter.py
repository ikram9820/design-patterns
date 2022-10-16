'''
Structural Design Patterns
Allows converting the interface of a class into another interface that clients expect.
'''

from abc import ABC, abstractmethod

class Target(ABC):
    @ abstractmethod
    def operation(self):
        pass

class Adopter(Target):
    def __init__(self) -> None:
        super().__init__()
        self.adoptee = Adoptee()

    def operation(self):
        pass

class Adoptee:
    def __init__(self) -> None:
        pass

    def otherOperation(self):
        pass

class Client:
    def __init__(self, target) -> None:
        self.target = target
    