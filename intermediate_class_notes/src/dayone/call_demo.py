from operator import itemgetter

class Square:
    def __call__(self, x):
        return x * x

class ItemGetter:
    def __init__(self, index):
        self.index = index

    def __call__(self, t):
        return t[self.index]


s = Square()
print(s(5))

t = "kashyap", "maduri", 0x1b, 'kashyap.mad@foobar.com'

get_age = ItemGetter(2)
new_get_age = itemgetter(2)

print(get_age(t))
print(new_get_age(t))
