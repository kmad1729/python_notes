'very basic building blocks in code'

delim = '*' * 20

class A:
    def method1(self, *args):
        print("this is method1")
        print("the are args ", args)

    def print_foo(self):
        print("foo")

def uppercase_all(*args):
    print('args -->', args)
    return list(map(str.upper, args))

def func_with_default_kwargs(x, debug = False, names = None):
    print('x -->', x)
    print('debug -->', debug)
    print('names -->', names)
    return "This is what i return! from func_with_default_kwargs"


def func_with_star_args(*args, **kwargs):
    print('args is a tuple of position args -->', args)
    print("kwargs is dict of keyword args -->", kwargs)

def func_python3_with_star(x, y, *, block = True):
    print("you cannot call this function with positional kwarg")
    print("x --> ", x)
    print("y --> ", y)
    print("block --> ", block)

######

print(delim)
print("this is a standalone statement")


print(delim)
a = A()
a.method1('hi','hello',1,3)
print(delim)

print(uppercase_all('foo', 'FO.{}DAScc'))
print(delim)

print(func_with_default_kwargs(10))
print(func_with_default_kwargs(10, names = 'ram raavan rahim'.split()))
print(func_with_default_kwargs(11, debug = True, names = 'foo bar'.split()))
print(delim)

func_with_star_args(10, 20, 30, 40, a = 1, b = 2, c = 3)
print(delim)


args1 = (1, 3, 5, 7, 9)
kwargs1 = {'x' : 24, 'y' : 25, 'z' : 26}
func_with_star_args(*args1, **kwargs1)
print(delim)

print("only in python3, '*' in arguments")

func_python3_with_star(y = 20, x = 10, block = 'foo')
try:
    print("calling function with block as positional arg!!")
    func_python3_with_star(10, 20, 30)
except TypeError as e:
    print("called the function with block as positional argument, got this exception -->")
    print('{', e, '}')

print(delim)

def sum_with_start(*args, initial_sum = 20):
    return initial_sum + sum(args)

print(sum_with_start(*range(10)))
print(sum_with_start(*range(10), initial_sum = 0))

s = sum_with_start(*range(10))

print(delim)
