#example.py

from debugly import debug

@debug(prefix = '***')
def add(x, y):
    return x + y

@debug
def sub(x, y):
    return x - y

@debug
def mul(x, y):
    return x * y

@debug(prefix = '***')
def div(x, y):
    return x / y

