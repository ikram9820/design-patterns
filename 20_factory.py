'''
Creational Design Patterns
Allows deferring the creation of an object to subclass.
'''

class Creator:
    def __init__(self) -> None:
        pass

    def operation(self):
        product = self.factoryMethod()

    def factoryMethod(self):
        pass

class ConcreteCreator(Creator):
    def __init__(self) -> None:
        super().__init__()

    def factoryMethod(self):
        return ConcreteCreator()
    
