# -- coding: utf-8 --
"""

Created on: 18/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""


#  Implement a calculator that can perform addition, subtraction,
#  multiplication, and division.


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return (self.num1 + self.num2)

    def subtract(self):
        return (self.num2 - self.num1)

    def multiply(self):
        return (self.num1 * self.num2)

    def divide(self):
        return (self.num2 / self.num1)


obj_1 = Calculator(10, 94)
print(f"num1: {obj_1.num1} y num2: {obj_1.num2}")
print("Addition:", obj_1.add())
print("Subtraction:", obj_1.subtract())
print("Multiply:", obj_1.multiply())
print("Division:", obj_1.divide())
