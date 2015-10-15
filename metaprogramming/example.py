#example.py

from debugly import debug, debugmethods, debugattr

@debug(prefix = '***')
def add(x, y):
    return x + y

@debug
def sub(x, y):
    return x - y

@debug
def mul(x, y):
    return x * y

@debug(prefix = '***')
def div(x, y):
    return x / y

@debugmethods
class Spam:

    def a(self):
        pass

    def b(self):
        pass

@debugattr
class Dog:

    def __init__(self, name):
        self.name = name

    def bark(self):
        return "Woof!, i am ", self.name

if __name__ == '__main__':
    delim = '*' * 20

    print(delim)
    print('add(2, 4) -->')
    print(add(2, 4))

    print(delim)
    print('add.__name__ -->')
    print(add.__name__)

    print(delim)
    print('sub(2, 4) -->')
    print(sub(2, 4))

    print(delim)
    print(delim)
    print("demonstrating debugmethods")

    s = Spam()
    s.a()

    print(delim)

    print(delim)
    print('demonstrating debug attr')
    d = Dog('fido')
    print(d.name)
    d.bark()
    print(delim)

