# -- coding: utf-8 --
"""

Created on: 21/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
#  A car is composed of an engine, tires, and doors. In this case, a Car
#  owned these objects, so a Car is an Owner class, and the tires, doors,
#  and engine classes are Owned classes.
class Engine:
    def __init__(self, capacity=0):
        self.capacity = capacity

    def printDetails(self):
        print("Engine Details:", self.capacity)

class Tires:
    def __init__(self, tires=0):
        self.tires = tires

    def printDetails(self):
        print("Number of tires:", self.tires)

class Door:
    def __init__(self, doors=0):
        self.doors = doors

    def printDetails(self):
        print("Number of doors:", self.doors)

class Car:
    def __init__(self, eng, tr, dr, color):
        self.eObj = Engine(eng)
        self.tObj = Tires(tr)
        self.dObj = Door(dr)
        self.color = color

    def printDetails(self):
        self.eObj.printDetails()
        self.tObj.printDetails()
        self.dObj.printDetails()
        print("Car color:", self.color)

car = Car(1600, 4, 2, "Grey")
car.printDetails()
