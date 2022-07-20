# -- coding: utf-8 --
"""

Created on: 20/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Shape
class Shape:
    def __init__(self, sides):
        self.sides = sides

    def getArea(self):
        pass

# Rectangle
class Rectangle(Shape):
    def __init__(self, width=0, height=0, sides=4):
        self.width = width
        self.height = height
        super().__init__(sides)

    def getArea(self):
        return  self.width * self.height

# Circle
class Circle(Shape):
    def __init__(self, radius=0, sides=0):
        self.radius = radius
        super().__init__(sides)

    def getArea(self):
        return self.radius * self.radius * 3.142

shapes = [Rectangle(6, 10), Circle(7)]
print("Area of rectangle is:", str(shapes[0].getArea()))
print("Area of rectangle is:", str(shapes[0].sides))
print("Area of circle is:", str(shapes[1].getArea()))
print("Area of rectangle is:", str(shapes[1].sides))


