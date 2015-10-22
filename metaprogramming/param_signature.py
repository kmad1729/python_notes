from inspect import Parameter, Signature

_fields = ['name', 'shares', 'price']

parms = [Parameter(f, Parameter.POSITIONAL_OR_KEYWORD) for f in _fields]

sig = Signature(parms)

def foo(*args, **kwargs):
    bound = sig.bind(*args, **kwargs)
    for name, val in bound.arguments.items():
        print(name, val)


f = foo(1,2,4)

