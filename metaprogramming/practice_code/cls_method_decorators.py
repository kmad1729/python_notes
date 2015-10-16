
from functools import partial, wraps

def debug(func = None, *, prefix = ''):
    if func is None:
        return partial(debug, prefix = prefix)
    msg = prefix + func.__qualname__ + prefix

    @wraps(func)
    def wrapper(*args, **kwars):
        print(msg)
        return func(*args, **kwars)
    return wrapper


@debug
def add(x, y):
    return x + y

@debug(prefix = '+++')
def mul(x, y):
    return x * y

######

def debugmethods(cls):
    'decorator for decorating methods in a class'
    for attr_str, attr_value in vars(cls).items():
        if callable(attr_value):
            print("this is decoration!")
            setattr(cls, attr_str, debug(attr_value))

    return cls


@debugmethods
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("bow bow, my name is ", self.name)

@debugmethods
class Car:
    def __init__(self, name):
        self.name = name

    @debug(prefix = '***')
    def honk(self):
        print("honk honk!")
