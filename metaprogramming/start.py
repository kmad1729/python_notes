#structly_with_inspect.py

class Structure:
    _fields = []
    def __init__(self, *args):
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

class Point(Structure):
    _fields = ['x', 'y']

class Address(Structure):
    _fields = ['hostname', 'port']
   
from inspect import Signature, signature

print('(signature(Stock)) -->', end = " ")
print(signature(Stock))
