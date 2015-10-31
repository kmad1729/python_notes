'Simple script showing how to use descriptors for type checking'

class descriptor:

    def __init__(self, name, inst_typ):
        self.name = name
        self.inst_type = inst_typ

    def __get__(self, instance, cls):
        print("getting inst var", self.name)
        return instance.__dict__[self.name]

    def __delete__(self, instance):
        print("deleting inst var", self.name)
        del instance.__dict__[self.name]

    def __set__(self, instance, val):
        print("setting inst var {} to val {}".format(self.name, val))
        if not isinstance(val, self.inst_type):
            raise TypeError(val, 'is not of type ', self.inst_type)
        instance.__dict__[self.name] = val

class Stock:

    _fields = ['name', 'shares', 'price']

    def __init__(self, *args, **kwargs):
        for k, v in zip(self.__class__._fields, args):
            setattr(self, k, v)

    shares = descriptor('shares', int)

s1 = Stock('GOOG', 100, 490.1)

print('trying to set shares to a string and catching a TypeError')

try:
    s1.shares = 'foo'
except TypeError as e:
    print('found exception ', e)
    

