from inspect import Signature, Parameter, signature
from functools import partial, wraps

class Descriptor:
    def __init__(self, name = None):
        self.name = name

    def __get__(self, instance, cls):
        print("get ", self.name)

    def __set__(self, instance, value):
        print("set {}'s {} to {}".format(self.name, instance, value))

    def __delete__(self, instance):
        print("delete {}',s {}".format(self.name, instance))

def debug(func = None, *, prefix = ''):
    if func == None:
        # debug called without arguments
        return partial(debug, prefix = prefix)
    msg = prefix + func.__qualname__ + prefix
    def func_wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return func_wrapper


def decorate_class_methods(cls):
    for k, v in vars(cls).items():
        if callable(v):
            setattr(cls, k, debug(v, prefix = "***"))
    return cls


@decorate_class_methods
class Structure:
    _fields = []
    def __init__(self, *args, **kwargs):
        for k, v in zip(self.__class__._fields, args):
            setattr(self, k, v)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

class Point(Structure):
    _fields = ['x', 'y']

    
s1 = Stock("GOOG", 100, 490.1)
