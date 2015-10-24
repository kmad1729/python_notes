from inspect import Parameter, Signature, signature

def make_signature(names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
                for name in names]
    return Signature(parms)


class Structure:
    __signature__ = make_signature([])

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for k, v in bound.arguments.items():
            setattr(self, k, v)

class Point(Structure):
    __signature__ = make_signature(['x', 'y'])

class Stock(Structure):
    __signature__ = make_signature(['name','shares','price'])

delim = '*' * 20
p1 = Point(1, 3)
print(signature(Point))
origin = Point(0, 0)
print(delim)
print(signature(Stock))
s1 = Stock(name = 'GOOG', price = 490.1, shares = '100')
print(delim)

