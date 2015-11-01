from inspect import Signature, Parameter

class Descriptor:
    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        print("Setting %s to %s" % (self.name, value))
        instance.__dict__[self.name] = value


    def __delete__(self, instance):
        print("Delete ", self.name)
        del instance.__dict__[self.name]


def make_signature(fields):
    return Signature(
            (Parameter(f, Parameter.POSITIONAL_OR_KEYWORD) for f in fields))

class StrucMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__new__(cls, clsname, bases, clsdict)
        clsobj.__signature__ = make_signature(clsobj._fields)
        return clsobj


class Structure(metaclass = StrucMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for k, v in bound.arguments.items():
            setattr(self, k, v)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

s1 = Stock('GOOG', 100, 490.1)
