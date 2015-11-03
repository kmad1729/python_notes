'simple demo of using map to create instances of objects'

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof! %s is barking!" % self.name)

dogs = list(map(Dog, ['rex', 'rover', 'ranger']))


