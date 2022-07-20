# -- coding: utf-8 --
"""

Created on: 20/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
class Shape:# Shape is a child class of ABC
    def area(self):
        pass

    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return self.length * 4

# objects
shape = Shape()
square = Square(4)

print(square.area())
print(square.perimeter())

print(shape.area())
print(shape.perimeter())

# abstract base classes  without abstract methods, area and perimeter #
from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length


shape = Shape()
# this code will not compile since Shape has abstract methods without
# method definitions in it
print(shape.area())



square = Square(4)
# this will code will not compile since abstarct methods have not been
# defined in the child class, Square
print(square.area())

# abstract base classes with abstract methods, area and perimeter #
# from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return self.length * 4

shape = Shape()
print(shape.area())

square = Square(4)
print(square.area())


class Parent:
    def prn(self):
        print("Parent")


class Child(Parent):
    def __init__(self):
        self.a = Parent()

    def prn(self):
        print("Child")


temp = Child()
temp.a.prn()
