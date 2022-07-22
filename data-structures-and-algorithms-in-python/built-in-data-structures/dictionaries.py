# -- coding: utf-8 --
"""

Created on: 22/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Creating a Dictionary #
empty_dict = {}  # Empty dictionary
print(empty_dict)

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

# The dict() Constructor #
empty_dict = dict()
print(empty_dict)

phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
# Keys will automatically be converted to strings
print(phone_book)

# Alternative approach
phone_book = ([('Batman',468426), ('Cersei', 237734),('Ghostbusters', 44678)])
print(phone_book)

# Accesing Values #
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}

print(phone_book["Cersei"])
print(phone_book.get("Cersei"))


