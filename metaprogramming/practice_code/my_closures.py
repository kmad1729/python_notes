from functools import partial

def my_decorator(func):
    print("this is executed from my_decorator")
    def wrapper(*args, **kwargs):
        print("this is executed from wrapper")
        print('func name -->', func.__qualname__)
        return func(*args, **kwargs)
    return wrapper

def decorator_with_args(prefix = ''):

    print(locals())
    def decorator(func):

        msg = prefix + func.__qualname__ + prefix
        print(locals())
        def wrapper(*args, **kwargs):
            print(msg)
            print(locals())
            return func(*args, **kwargs)
        return wrapper

    return decorator

from functools import partial
def my_decorator(func = None, *, prefix = ''):
    if func is None:
        return partial(my_decorator, prefix = prefix)

    msg = prefix + func.__qualname__ + prefix
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper




@my_decorator
def add(x, y):
    print("function add is called")
    return x + y

@my_decorator(prefix = '###')
def mul(x, y):
    print("function mul is called")
    return x * y


a = my_decorator(add)

def awesome_function(a = 0, b = 0, *, prefix):
    print('a ->', a)
    print('b ->', b)
    print('prefix ->', prefix)
    return prefix + str(a+b)
