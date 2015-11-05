from inspect import Signature, Parameter

class Descriptor:
    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        print("Setting %s to %s" % (self.name, value))
        instance.__dict__[self.name] = value


    def __delete__(self, instance):
        print("Delete ", self.name)
        del instance.__dict__[self.name]

class Typed(Descriptor):
    ty = object
    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise TypeError("Expected %s" % self.ty)
        #not the parent but next class on mro list
        super().__set__(instance, value)    

#here is a good use of keyword only arguments
class Sized(Descriptor):
    
    def __init__(self, *args, maxlen, **kwargs):
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)

    def __set__(self, instance, val):
        if len(val) > self.maxlen:
            raise ValueError('%s exceeds the maximum len %s' % \
                    (val, self.maxlen))
        super().__set__(instance, val)

import re
class Regex(Descriptor):
    def __init__(self, *args, pat, **kwargs):
        self.pat = re.compile(pat)
        super().__init__(*args, **kwargs)

    def __set__(self, instance, val):
        if not self.pat.match(val):
            raise ValueError("%s does not match pattern %s" % \
                    (val, self.pat))
        super().__set__(instance, val)


class Integer(Typed):
    ty = int
class String(Typed):
    ty = str
class Float(Typed):
    ty = float

class Positive(Descriptor):
    def __set__(self, instance, val):
        if val < 0:
            raise ValueError("%s must be >= 0" % val)
        super().__set__(instance, val)

class PositiveInteger(Integer, Positive):   #mixin class
    pass

class SizedRegexString(Sized, Regex, String):
    pass
class PositiveFloat(Float, Positive):
    pass

def make_signature(fields):
    return Signature(
            (Parameter(f, Parameter.POSITIONAL_OR_KEYWORD) for f in fields))

class StrucMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__new__(cls, clsname, bases, clsdict)
        clsobj.__signature__ = make_signature(clsobj._fields)
        return clsobj


class Structure(metaclass = StrucMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for k, v in bound.arguments.items():
            setattr(self, k, v)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']
    name = SizedRegexString('name', maxlen = 8, pat = r'[A-Z]+')
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')

s1 = Stock('GOOG', 100, 490.1)
