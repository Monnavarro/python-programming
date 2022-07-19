# -- coding: utf-8 --
"""

Created on: 18/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

#Implement a constructor to initialize the values of two private properties:
# length and width.
#Implement a method, area(), in the Rectangle class that returns the product
# of length and width. See the formula below:
# Area = length x width
# Implement a method, perimeter(), in the Rectangle class that returns
# two times the sum of length and width. See the formula below:
# Perimeter = 2 x (length + width)

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return(self.__length * self.__width)

    def perimeter(self):
        return(2 * (self.__length + self.__width))

rect_1 = Rectangle(4, 5)
print(rect_1.area())
print(rect_1.perimeter())


