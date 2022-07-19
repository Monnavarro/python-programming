# -- coding: utf-8 --
"""

Created on: 18/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
"""
Implement the following properties as private:
* name
* rollNumber

Include the following methods to get and set the private properties above:
* getName()
* setName()
* getRollNumber()
* setRollNumber()

Implement this class according to the rules of encapsulation.
"""
class Student:
    __name = None
    __rollNumber = None

    def setName(self, x):
        self.__name = x

    def getName(self):
        return(self.__name)

    def setRollNumber(self, Y):
        self.__rollNumber = Y

    def getRollNumber(self):
        return(self.__rollNumber)


student_1 = Student()
print(student_1.getName())
student_1.setName('Paloma')
print(student_1.getName())
student_1.setRollNumber(999999)
print(student_1.getRollNumber())


