class Square:
    def __call__(self, x):
        return x * x

s = Square()
print(s(5))
