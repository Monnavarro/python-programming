# -- coding: utf-8 --
"""

Created on: 19/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Example
class Vehicle: # defining the parent class
    fuelCap = 90

class Car(Vehicle):
    fuelCap = 50

    def display(self):
        # accessing fuelCap from the Vehicle Class using super()
        print("Fuel cap from the Vehicle Class:", super().fuelCap)

        # accessing fuelCap from the Car Class using self
        print("Fuel cap from the Car Class:", self.fuelCap)


obj1 = Car()  # creating a car object
obj1.display()  # calling the Car class method display()

# Calling the parent class methods #
class Vehicle:  # defining the parent class
    def display(self):  # defining display method in the parent class
        print("I am from the Vehicle Class")

class Car(Vehicle):  # defining the child class
    def display(self):  # defining display method in the child class
        super().display()
        print("I am from the Car Class")


obj1 = Car()  # creating a car object
obj1.display()  # calling the Car class method display()

# USing with initializers #
# function super() made in the second line of the method.
class ParentClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b

class ChildClass(ParentClass):
    def __init__(self, a, b, c):
        self.c = c
        super().__init__(a, b)

obj = ChildClass(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)


# function super() made in the first line of the method.
class ParentClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b

class ChildClass(ParentClass):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

obj = ChildClass(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)


# Example Clas Vehicle
class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)

class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        super().__init__(make, color, model)  # change for function super()
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Door:", self.doors)


obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printCarDetails()