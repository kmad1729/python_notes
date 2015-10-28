class A:
    def __init__(self, x):
        self.x = x

    def __cmp__(self, other):
        return cmp(self.x,  other.x)

    def __repr__(self):
        return str(self.x)


a, b, c = map(A, [10, 20, 0])

print(sorted([a, b, c]))
