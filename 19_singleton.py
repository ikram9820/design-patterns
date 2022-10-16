'''
Creational Design Patterns
To ensure an object has only a single instance.
'''


class Singleton:
    _object = None
    def __init__(self) -> None:
        if Singleton._object is None:
            Singleton._object = self

    def getInstance(self):
        return Singleton._object

o1 = Singleton()
o2 = Singleton()
print(o1.getInstance(),o2.getInstance())