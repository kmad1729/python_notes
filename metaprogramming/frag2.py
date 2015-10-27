#!/usr/bin/env python3

from inspect import Signature, Parameter, signature

def make_signature(names):
    return Signature(
            [Parameter(f, Parameter.POSITIONAL_OR_KEYWORD) 
            for f in names])

class StructMeta(type):
    def __new__(cls, cls_name, bases, cls_dict):
        cls_obj = super().__new__(cls, cls_name, bases, cls_dict)
        sig = make_signature(cls_obj._fields)
        setattr(cls_obj, '__sigature__', sig)
        return cls_obj
    

class Stucture(metaclass = StructMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound = self.__sigature__.bind(*args, **kwargs)
        for k, v in bound.arguments.items():
            setattr(self, k, v)

    def __repr__(self):
        args = ', '.join([repr(getattr(self, name))
                for name in self._fields])
        return type(self).__name__ + '(' + args + ')'

class Stock(Stucture):
    _fields = ['name', 'shares', 'price']

class Point(Stucture):
    _fields = ['x', 'y']

s1 = Stock("GOOG", 100, 490.1)
s2 = Stock(shares = 299, name = "CSCO", price = "29.29")
