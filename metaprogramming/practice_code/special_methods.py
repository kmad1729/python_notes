class MyArray:
    def __init__(self, *args):
        self.elems = list(args)

    def __repr__(self):
        return str(self.elems)

    def __getitem__(self, index):
        return self.elems[index]

    def __setitem__(self, index, value):
        self.elems[index] = value

    def __delitem__(self, index):
        del self.elems[index]

    def __contains__(self, item):
        return item in self.elems

delim = '*' * 20

m_a = MyArray(*(range(0, 20, 3)))
print('MyArray m_a -->', m_a)
print(delim)

ind = 2
print('m_a[', ind, '] = ', m_a[ind])
print(delim)

new_val = 42
print("setting value ", new_val, " to index ", ind)
m_a[ind] = new_val
print('MyArray m_a -->', m_a)
print(delim)

ind = 0
print("delete item from index", ind)
del m_a[ind]
print('MyArray m_a -->', m_a)
print(delim)

print("checking if ", new_val, " in m_a")
print(new_val in m_a)
print('MyArray m_a -->', m_a)
print(delim)

