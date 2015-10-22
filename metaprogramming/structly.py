class Structure:
    _fields = []
    def __init__(self, *args):
        for k, v in zip(self.__class__._fields, args):
            setattr(self, k, v)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

class Point(Structure):
    _fields = ['x','y']

class Address(Structure):
    _fields = ['hostname', 'port']


s = Stock("GOOG", 100, 490.1)



