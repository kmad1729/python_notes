
def make_adder(x, y):
    def add():
        return x + y
    return add

a = make_adder(2, 4)
b = make_adder(40, 20)

print(a())
print(b())
