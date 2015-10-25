from inspect import Signature, Parameter, signature

def make_signature(names):
    return Signature([
            Parameter(f, Parameter.POSITIONAL_OR_KEYWORD)
            for f in names])

def add_signature(*names):
    def decorate(cls):
        cls.__signature__ = make_signature(names)
        return cls
    return decorate

class Structure:
    __signature__ = make_signature([])
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for k, v in bound.arguments.items():
            setattr(self, k, v)

@add_signature('x', 'y')
class Point(Structure):
    pass

@add_signature('name', 'shares', 'price')
class Stock(Structure):
    pass

#Stock = add_signature('name', 'shares', 'price')(Stock)
#    ---> decorate(Stock) with access to "names" variable 

s1 = Stock('GOOG', 100, 490.1)
s2 = Stock('CSCO', price = 29.25, shares = 333)
s3 = Stock('AAPL', price = 112.11, shares = 1900)



