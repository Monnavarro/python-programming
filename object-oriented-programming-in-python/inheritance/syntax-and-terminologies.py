# -- coding: utf-8 --
"""

Created on: 19/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Example of Pantent Class and Child Class

class ParentClass:
    pass
    # atributes of the parent class

class ChildClass(ParentClass):
    pass
    # atributes of the child class

# Example with Vehicle Class #

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
    def __init__(self,make, color, model, doors):
        # calling the constructor from parent class
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Doors:", self.doors)


obj_1 = Car("Suzuki", "Grey", "2015", 4)
obj_1.printCarDetails()