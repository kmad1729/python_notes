
class Dog():
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("hi i am ", self.name, " woof!!")

class AggressiveDog(Dog):

    def bark(self):
        print("I am an aggreesive dog!")
        return super(AggressiveDog, self).bark()

delim = '*' * 20
print(delim)
d1 = Dog('Fido')
d1.bark()
print(delim)
d2 = AggressiveDog('Super fido')
d2.bark()
