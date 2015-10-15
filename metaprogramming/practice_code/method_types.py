class Spam():

    def __init__(self, name):
        self.name = name

    def imethod(self):
        print('this is an instance method!')
        print("self.name -->", self.name)
        print("self -->", self)

    @classmethod
    def cmethod(cls):
        print("this is class method")
        print("cls -->", cls)
        return(cls(32))

    @staticmethod
    def smethod():
        print("this is a static method")
        print('2 + 2 -->', 2 + 2)

delim = '*' * 20
print(delim)
print("calling instance method -->")
s = Spam(42)
print(s.imethod())
print(delim)
print("calling class method -->")
print(Spam.cmethod())
print(delim)
print("calling static mehtod -->")
print(Spam.smethod())
print(delim)
