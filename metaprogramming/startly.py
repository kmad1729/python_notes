#startly.py
#show how to use Parameter and Signature from inspect module

from inspect import Parameter, Signature

def make_signature(names):
    return Signature(
            Parameter(f, Parameter.POSITIONAL_OR_KEYWORD)
            for f in names)



class Structure:

    __signature__ = make_signature([])
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']
    __signature__ = make_signature(_fields[:])

class Point(Structure):
    _fields = ['x', 'y']

class Address(Structure):
    _fields = ['hostname', 'port']
   
from inspect import Signature, signature

print('(signature(Stock)) -->', end = " ")
print(signature(Stock))

s1 = Stock("GOOG", 100, 490.1)
s2 = Stock(name = "CSCO", price = 28.99, shares = 800)
try:
    print("calling stock with 4 arguments")
    s3 = Stock(22, 4, 3, 43)
except TypeError as e:
    print("encountered TypeError -->", e)
