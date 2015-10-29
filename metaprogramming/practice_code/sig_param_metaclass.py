from inspect import Signature, Parameter, signature


def make_signature(fields):
    return Signature(
            [Parameter(f, Parameter.POSITIONAL_OR_KEYWORD)
            for f in fields])

class StructMeta(type):
    def __new__(cls, cls_name, bases, cls_dict):
        cls_obj = super().__new__(cls, cls_name, bases, cls_dict)
        cls_obj.__signature__ = make_signature(cls_obj._fields)
        return cls_obj


class Structure(metaclass = StructMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for k, v in bound.arguments.items():
            setattr(self, k, v)

    def __repr__(self):
        args = ', '.join([repr(getattr(self, name))
            for name in self._fields])
        return type(self).__name__ + '(' + args + ')'
        '''
        result = self.__class__.__name__ + "(" +  \
        ', '.join([str(getattr(self, f)) for f in self.__class__._fields]) \
        +  ")"
        return result
        '''

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

class Point(Structure):
    _fields = ['x', 'y']

s1 = Stock('GOOG', 100, 490.1)
s2 = Stock(price = 29.25, name = 'CSCO', shares = 100)





