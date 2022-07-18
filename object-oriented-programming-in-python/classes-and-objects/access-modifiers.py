# -- coding: utf-8 --
"""

Created on: 18/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Public Attributes
class Employee:
    def __init__(self, ID, salary):
        # all properties are public
        self.ID = ID
        self.salary = salary

    def displayID(self):
        print("ID:", self.ID)

Steve = Employee(3789, 2500)
Steve.displayID()
print(Steve.salary)


# Private Attributes
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property

Steve = Employee(3789, 2500)
print("ID:", Steve.ID)
print("Salary:", Steve.__salary)  # this will cause an error


# Private methods
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary # salary is a private property

    def displaySalary(self):  # displaySalary is a public method
        print("Salary:", self.__salary)

    def __displayID(self): # displaySalary is a private method
        print("ID:", self.ID)

Steve = Employee(3789, 2500)
Steve.displaySalary()
Steve.__displayID()  # this will generate an error



# Accessing private attributes in the main code
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary   # salary is a private property

Steve = Employee(3789, 2500)
print(Steve._Employee__salary)  # accessing a private property







