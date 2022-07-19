# -- coding: utf-8 --
"""

Created on: 19/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Single Inheritance #
class Vehicle:  # parent class
    def setTopSpeed(self, speed):  # defining the set
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)

class Car(Vehicle):  # child class
    def openTrunk(self):
        print("Trunk is now open.")

corolla = Car()  # creating an object of the Car class
corolla.setTopSpeed(300)  # accessing methods from the parent class
corolla.openTrunk()  # accessing method from its own class

# Multi-level inheritance #
class Vehicle: # parent class
    def setTopSpeed(self, speed):
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)

class Car(Vehicle):  # child class of Vehicle
    def openTrunk(self):
        print("Trunk is now open")

class Hybrid(Car):  # child class of Car
    def turnOnHybrid(self):
        print("Hybrid mode is now switched on.")

prius = Hybrid()  # creating an object of the Hybrid class
prius.turnOnHybrid()  # accessing method from the child class
prius.openTrunk()  # accessing method from the parent class
prius.setTopSpeed(600)  # accessing methods from the parent class

# Hierarchical Inheritance #
class Vehicle:  # parent class
    def setTopSpeed(self, speed):
        self.topSpeed = speed  # defining the set
        print("Top speed is set to", self.topSpeed)

class Car(Vehicle):  # child class of Vehicle
    pass

class Truck(Vehicle):  # child class of Vehicle
    pass

corolla = Car()  # creating an object of the Car class
corolla.setTopSpeed(150)   # accessing methods from the parent class

volvo = Truck()  # creating an object of the Truck class
volvo.setTopSpeed(300)  # accessing methods from the parent class


# Multiple Inheritance #
class CombustionEngine:
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity

class ElectricEngine():
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# Child class inherited from CombustionEngine and ElectricEngine
class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)

car = HybridEngine()
car.setChargeCapacity("250 W")
car.setTankCapacity("20 litres")
car.printDetails()

# Hybrid Inherited #
class Engine:  # parent class
    def setPower(self, power):
        self.power = power

class CombustionEngine(Engine):  # Child class inherited from Engine
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity

class ElectricEngine(Engine):  # Child class inherited from Engine
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# Child class inherited from CombustionEngine and ElectricEngine
class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Power:", self.power)
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)

car = HybridEngine()
car.setPower("2000 CC")
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()




