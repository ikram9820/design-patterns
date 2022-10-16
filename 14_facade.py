'''
Structural Design Patterns
Provides a simplified, higher-level interface to a subsystem. Clients 
can talk to the facade rather than individual classes in the subsystem.
'''

class Facade:
    def __init__(self) -> None:
        pass

class Client:
    def __init__(self,facade) -> None:
        self.facade = facade