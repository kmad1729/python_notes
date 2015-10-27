#debugly.py

from functools import  wraps, partial

def debug(func=None, *, prefix = ''):
    if func is None:
        return partial(debug, prefix = prefix)
    #func is function to be wrapped
    msg = prefix + func.__qualname__ + prefix
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper

def debugmethods(cls):
    #cls is a class
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))

    return cls

def debugattr(cls):
    orig_getattribute = cls.__getattribute__

    def __getattribute__(self, name):
        print("Get:", name)
        return orig_getattribute(self, name)

    cls.__getattribute__ = __getattribute__
    return cls
