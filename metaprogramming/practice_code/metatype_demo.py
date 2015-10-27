from cls_method_decorators import debugmethods

class metatype(type):
    def __new__(cls, cls_name, bases, cls_dict):
        clsobj = super().__new__(cls, cls_name, bases, cls_dict)
        clsobj = debugmethods(clsobj)
        return clsobj


class Animal(metaclass = metatype):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("hi, my name is ", self.name)

class Dog(Animal):

    def greet(self):
        print("Woof!, my name is", self.name)

class Cat(Animal):

    def greet(self):
        print("meow!, my name is", self.name)




