# -- coding: utf-8 --
"""

Created on: 22/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Creating a Tuple #
car = ("Ford", "Raptor", 2019, "Red")
print(car)

# length
print(len(car))

# Indexing #
print(car[1])

# Slicing #
print(car[2:])

# Merging Tuples #
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = hero1 +hero2
print(awesome_team)

# Nested Tuples #
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = (hero1, hero2)
print(awesome_team)

# Search #
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Moscow" in cities)
print("Paris" in cities)

# the index() function #
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print(cities.index("Tokyo"))

