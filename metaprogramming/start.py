#start.py

class Structure:
    _fields = []
    def __init__(self, *args):
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

class Sock(Structure):
    _fields = ['name', 'shares', 'price']

class Point(Structure):
    _fields = ['x', 'y']

class Address(Structure):
    _fields = ['hostname', 'port']
   
