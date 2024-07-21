class Animal:  # main class
    def walk(self):
        print("Walking...")


class Dog(Animal):  # inherited class from Animal
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    def speak(self):
        print("Woof!")

    def __gt__(self, other):  # comparison; greater than
        return True if self.age > other.age else False


# Polymorphism
class Cat(Animal):  # inherited class from Animal
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    def speak(self):
        print("Meow!")


roger = Dog("Roger", 8)
syd = Dog("Syd", 7)
kitty = Cat("Kitty", 5)
print(type(roger))  # print the type of "roger", it will be class __main__.Dog
print(roger.name)  # print the name
print(roger.age)  # print the age
roger.walk()
roger.speak()  # polymorphism
kitty.speak()  # polymorphism
print(roger > syd)  # operator overloading

"""
Other methods:
__gt__() - greater than
__lt__() - less than
__le__() - less or equal to
__ge__() - greater or equal to
__add__() - + operator
__sub__() - - operator
__mul__() - * operator
__truediv__() - / operator
__floordiv__() - // operator
__mod__() - % operator
__pow__() - ** operator
__and__() - & operator
__or__() - | operator
__xor__() - ^ operator
"""
