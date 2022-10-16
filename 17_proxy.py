'''
Structural Design Patterns
Allows providing a substitute for another object. The proxy object delegates 
all the work to the target object and contains some additional behavior.
'''

class Subject:
    def __init__(self) -> None:
        pass

    def request(self):
        pass

class RealSubject(Subject):
    def __init__(self) -> None:
        super().__init__()

    def request(self):
        return super().request()
    
class Proxy(Subject):
    def __init__(self) -> None:
        super().__init__()
        self.realSubject = RealSubject()
    
    def request(self):
        self.realSubject.request()

class Client:
    def __init__(self,subject) -> None:
        self.subject = subject
        