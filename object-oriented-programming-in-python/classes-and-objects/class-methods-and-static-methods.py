# -- coding: utf-8 --
"""

Created on: 18/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
class Myclass:
    classVariable = 'educative'

    @classmethod
    def demo(cls):
        return cls.classvariable

# code implementation for class method
class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @classmethod
    def getTeamName(cls):
        return cls.teamName

print(Player.getTeamName())


# Static method #
class Player:
    teamName = 'Liverpool'

    def __init__(self, name):
        self.name = name

    @staticmethod
    def demo():
        print("I am  a static method")
p1 = Player('lol')
p1.demo()
Player.demo()
print(p1.name)


# We can make a static method for calculating the BMI of any given
# weight and height:
class BodyInfo:

    @staticmethod
    def bmi(weight, height):
        return weight / height

weight = 75
height = 1.8
print(BodyInfo.bmi(weight,height))

