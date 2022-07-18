# -- coding: utf-8 --
"""

Created on: 18/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

# Implement a class Point that has three properties and a method.
# All these attributes (properties and methods) should be public.

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return((self.x * self.x ) + (self.y * self.y ) + (self.z * self.z))


Obj_1 = Point(1, 3, 5)
print(Obj_1.x, Obj_1.y, Obj_1.z)
print(Obj_1.sqSum())


# other solution
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        a = self.x * self.x
        b = self.y * self.y
        c = self.z * self.z
        return(a + b + c)


obj1 = Point(4, 5, 6)
print(obj1.sqSum())