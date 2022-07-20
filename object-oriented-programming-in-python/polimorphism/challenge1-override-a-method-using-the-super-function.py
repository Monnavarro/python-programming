# -- coding: utf-8 --
"""

Created on: 20/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# When a method in a derived class overrides a method in a base class,
# it is still possible to call the overridden method using
# the super() function.
class Shape:
    def __init__(self, sname="Shape"):
        self.sname = sname

    def getName(self):
        pass


class XShape(Shape):
    # initializer
    def __init__(self, name, sname="Shape"):
        super().__init__(sname)
        self.xsname = name

    def getName(self):  # overriden method
        return self.sname +  ", " + self.xsname

circle = XShape("Circle")
Rectangle = XShape("Rectangle")
circle.getName()
Rectangle.getName()

# Other solution
class Shape:
    sname = "Shape"

    def getName(self):
        return self.sname

class XShape(Shape):
    # initializer
    def __init__(self, name):
        self.xsname = name

    def getName(self):  # overriden method
        return super().getName() +  ", " + self.xsname
