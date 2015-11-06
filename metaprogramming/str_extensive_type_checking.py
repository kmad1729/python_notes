'making a type checked Stock class'

from inspect import Signature, Parameter
import re
from collections import OrderedDict

def make_signature(names):
    return Signature(
            [Parameter(n, Parameter.POSITIONAL_OR_KEYWORD) for n in names])



class Descriptor:
    def __set__(self, instance, val):
        print("setting %s to %s" % (self.name, val))
        instance.__dict__[self.name] = val

    def __delete__(self, instance):
        print("deleting %s" % self.name)
        del instance.__dict__[self.name]

class Typed(Descriptor):
    ty = object

    def __set__(self, instance, val):
        if not isinstance(val, self.ty):
            raise TypeError("%s is not of type %s" % (val, self.ty))
        super().__set__(instance, val)

class Positive(Typed):

    def __set__(self, instance, val):
        if val < 0:
            raise ValueError("%s should be >= 0" % val)
        super().__set__(instance, val)

class Integer(Typed):
    ty = int

class Float(Typed):
    ty = float

class String(Typed):
    ty = str

class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class Regex(Descriptor):
    def __init__(self, *args, pat, **kwargs):
        self.pat = re.compile(pat)
        super().__init__(*args, **kwargs)

    def __set__(self, instance, val):
        if not self.pat.match(val):
            raise ValueError("%s does not match pattern %s" % (val, self.pat))
        super().__set__(instance, val)

class Sized(Descriptor):
    def __init__(self, *args, maxlen, **kwargs):
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)

    def __set__(self, instance, val):
        if len(val) > self.maxlen:
            raise ValueError("max len of (%s) can be %s" % \
                    (self.name, self.maxlen))
        super().__set__(instance, val)

class StringRegexSized(String, Regex, Sized):
    pass

class StructMeta(type):

    def __prepare__(cls_name, bases):
        return OrderedDict()

    def __new__(cls, cls_name, bases, cls_dict):
        fields = [k for k, v in cls_dict.items() if isinstance(v, Descriptor)]

        for f in fields:
            cls_dict[f].name = f

        cls_obj = super().__new__(cls, cls_name, bases, dict(cls_dict))
        cls_obj.__signature__ = make_signature(fields)

        return cls_obj

class Structure(metaclass = StructMeta):

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for k, v in bound.arguments.items():
            setattr(self, k, v)

class Stock(Structure):
    name = StringRegexSized(pat = r'[A-Z]+', maxlen = 8)
    shares = PositiveInteger()
    price = PositiveFloat()

if __name__ == '__main__':
    s1 = Stock("GOOG", 100, 490.1)
