class CEO:
    __shared_state= {
        "name": "steve",
        "age": 55
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f"{self.name} {self.age}"

class Monostate:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state

class CFO(Monostate):

    def __init__(self):
        self.name = ""
        self.money_managed = 0
    
    def __str__(self):
        return self.name