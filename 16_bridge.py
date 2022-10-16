'''
Structural Design Patterns
Allows representing hierarchies that grow in two different dimensions independently.
'''

class Device:
    def __init__(self) -> None:
        pass

    def turnOn(self):
        pass

class RemoteControl:
    def __init__(self) -> None:
        self.device = Device()
    
    def turnOn(self):
        self.device.turnOn()

class SonyTv(Device):
    def __init__(self) -> None:
        super().__init__()

class AdvancedRemote(RemoteControl):
    def __init__(self) -> None:
        super().__init__()