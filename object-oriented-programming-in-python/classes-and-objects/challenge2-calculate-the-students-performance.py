# -- coding: utf-8 --
"""

Created on: 18/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Implement a constructor to initialize the values of four
# properties: name, phy, chem, and bio.

# Implement a method – totalObtained – in the Student class that
# calculates total marks of a student.

# Using the totalObtained method, implement another method, percentage, in
# the Student class that calculates the percentage of students marks. Assume
# that the total marks of each subject are 100. The combined marks
# of three subjects are 300.

class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        total = self.phy + self.chem + self.bio
        return(total)

    def percentage(self):
        percent = (self.totalObtained() / 300) * 100
        return percent


obj_1 = Student('Mark', 80, 90, 40)
print("name =", obj_1.name)
print("phy =", obj_1.phy)
print("chem =", obj_1.chem)
print("bio =", obj_1.bio)

print("Total :", obj_1.totalObtained())
print("Percentage :", obj_1.percentage())

