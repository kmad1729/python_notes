from functools import partial

def my_decorator(func = None, *, prefix = ''):
    if func is None:
        return partial(my_decorator, prefix = prefix)
    def wrap(func_name):
        pass

def func_with_start(a, b, *, debug = False):
    result = a + b
    if debug:
        print('a = {}, b = {}'.format(a, b))
        print('a + b = {}'.format(result))
    return result


