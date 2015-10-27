
from functools import partial

def debug(func = None, *, prefix = ''):
    if func is None:
        print("this is executed when decorator is called with args")
        return partial(debug, prefix = prefix)

    msg = prefix + func.__qualname__ + prefix

    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)

    return wrapper


@debug
def sum(x, y):
    return x + y

@debug(prefix = '###')
def mul(x, y):
    return x * y
