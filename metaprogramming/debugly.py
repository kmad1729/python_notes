#debugly.py

from functools import  wraps, partial

def debug(func=None, *, prefix = ''):
    if func is None:
        return partial(debug, prefix = prefix)
    print('func adfadfad', func.__name__)
    #func is function to be wrapped
    msg = prefix + func.__qualname__ + prefix
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper

#Done till 19:00
