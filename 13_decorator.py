'''
Structural Design Patterns
Adds additional behavior to an object dynamically.
'''
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation():
        pass

class ConcreteComponent(Component):
    def __init__(self) -> None:
        super().__init__()

    def operation(self):
        pass

class Decorator(Component):
    def __init__(self) -> None:
        super().__init__()
        self.component = Component()
    
    def operation(self):
        self.component.operation()