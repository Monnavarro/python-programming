# -- coding: utf-8 --
"""

Created on: 21/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Let’s take the example of people and their country of origin. Each person
# is associated with a country, but the country can exist without that person.
class Country:
    def __init__(self, name=None, population=0):
        self.name = name
        self.population = population

    def printDetails(self):
        print("Country Name:", self.name)
        print("Country Population:", self.population)

class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def printDetails(self):
        print("Person Name:", self.name)
        self.country.printDetails()

c = Country("Mexico", 8000)
p = Person("Montserrat", c)
p.printDetails()


# delete the object p of Person Class
del p
print("")
c.printDetails()
