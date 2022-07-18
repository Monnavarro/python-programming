# -- coding: utf-8 --
"""

Created on: 18/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Defining class variables and instance variables
class Player:
    teamName = 'Canada'  # class variables

    def __init__(self, name):
        self.name = name # creating instance variables

p1 = Player('Mark')
p2 = Player('Lazaro')

print("Name :", p1.name)
print("Team Name", p1.teamName)
print("Name :", p2.name)
print("Team Name", p2.teamName)

# Wrong use of class variables
class Player:
    formerTeams = []  # class variables
    teamName = 'Liverpool'
    def __init__(self, name):
        self.name = name  # creating instance variables

p1 = Player('Mark')
p2 = Player('Lazaro')

p1 = Player('Mark')
p1.formerTeams.append('Barcelona')  # wrong use of class variable
p2 = Player('Lazaro')
p2.formerTeams.append('Chelsea')  # wrong use of class variable

print("Name :", p1.name)
print("Team Name", p1.teamName)
print(p1.formerTeams)
print("Name :", p2.name)
print("Team Name", p2.teamName)
print(p2.formerTeams)

# Correction
class Player:
    teamName = 'Liverpool'  # class variables
    def __init__(self, name):
        self.name = name  # creating instance variables
        self.formerTeams = []

p1 = Player('Mark')
p2 = Player('Lazaro')

p1 = Player('Mark')
p1.formerTeams.append('Barcelona')  # wrong use of class variable
p2 = Player('Lazaro')
p2.formerTeams.append('Chelsea')  # wrong use of class variable

print("Name :", p1.name)
print("Team Name", p1.teamName)
print(p1.formerTeams)
print("Name :", p2.name)
print("Team Name", p2.teamName)
print(p2.formerTeams)


# Using class variables smartly
class Player:
    teamName = 'Liverpool'
    teamMembers = []

    def __init__(self, name):
        self.name = name  # creating instance variables
        self.formerTeams = []
        self.teamMembers.append(self.name)

p1 = Player('Mark')
p1.formerTeams.append('Barcelona')
p2 = Player('Steve')
p2.formerTeams.append('Chelsea')


print("Name:", p1.name)
print("Team Members:")
print(p1.teamMembers)
print(p1.formerTeams)
print("")
print("Name:", p2.name)
print("Team Members:")
print(p2.teamMembers)
print(p2.formerTeams)

