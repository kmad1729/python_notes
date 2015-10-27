from cls_method_decorators import add, mul, Dog, Car

'use of cls_method_decoratos'

delim = '*' * 20

print(delim)
x = 10
y = 20
print("add({}, {}) -->".format(x, y))
print(add(x, y))
print(delim)

x = 23
y = 22
print("mul({}, {}) -->".format(x, y))
print(mul(x, y))
print(delim)

d = Dog('fido')
d.bark()
d.name = "tommy"
print(delim)

c = Car('honda')
c.honk()
print(delim)
