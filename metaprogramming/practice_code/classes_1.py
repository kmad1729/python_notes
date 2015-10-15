delim = "*" * 20
class Spam:
    a = 1

    def __init__(self, b):
        self.b = b
        
    def imethod(self):
        print("inside instance method")
        pass

print(delim)
print("class variable a -->", Spam.a)

print(delim)
s = Spam(2)
print("instance variable b -->", s.b)
print(delim)

print("instance method of s -->", s.imethod())
print(delim)
