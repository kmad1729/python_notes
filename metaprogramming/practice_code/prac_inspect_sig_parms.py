from inspect import Signature, signature, Parameter

_fields = ['name', 'shares', 'price']

parms = [Parameter(field, Parameter.POSITIONAL_OR_KEYWORD) for field in _fields]

sig = Signature(parms)


def foo(*args, **kwargs):
    #--> sig.bind binds the arguments of foo to sig
    bound = sig.bind(*args, **kwargs)
    for k, v in bound.arguments.items():
        print(k, v)

foo(1,2,3)
foo(name = "GOOG", price = 490.1, shares = 100)

