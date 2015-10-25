from inspect import Signature, Parameter, signature

def make_signature(names):
    return Signature([Parameter(n, Parameter.POSITIONAL_OR_KEYWORD)
        for n in names])


class Structure:
    __signature__ = make_signature([])

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for k,v in bound.arguments.items():
            setattr(self, k, v)

class Stock(Structure):
    __signature__ = make_signature(['name', 'shares', 'price'])

class Point(Structure):
    __signature__ = make_signature(['x','y'])


s = Stock("GOOG", 100, 490.1)



