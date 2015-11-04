from inspect import Signature, Parameter

class Descriptor:
    def __init__(self, name):
        self.name = name

    def __set__(self, instance, val):
        print("setting %s to %s" % (self.name, val))
        instance.__dict__[self.name] = val

    def __delete(self, instance):
        print("deleting %s from instance" % (self.name))
        del instance.__dict__[self.name]

class Typed(Descriptor):
    ty = object

    def __set__(self, instance, val):
        if not isinstance(val, self.ty):
            raise TypeError("%s is not of type %s" % (val, self.ty))
        super().__set__(instance, val)

class Positive(Descriptor):
    def __set__(self, instance, val):
        if val < 0:
            raise ValueError("%s must be >= 0" % val)
        super().__set__(instance, val)


class Integer(Typed):
    ty = int

class String(Typed):
    ty = str

class Float(Typed):
    ty = float

class PostiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass


def make_signature(names):
    return Signature(
            [Parameter(n, Parameter.POSITIONAL_OR_KEYWORD)
                for n in names])
            
class StructMeta(type):
    def __new__(cls, cls_name, bases, cls_dict):
        cls_obj = super().__new__(cls, cls_name, bases, cls_dict)
        cls_obj.__signature__ = make_signature(cls_obj._fields)
        return cls_obj

class Structure(metaclass = StructMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for k, v in bound.arguments.items():
            setattr(self, k, v)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']
    name = String('name')
    shares = PostiveInteger('shares')
    price = PositiveFloat('price')


s1 = Stock("GOOG", 100, 490.1)
