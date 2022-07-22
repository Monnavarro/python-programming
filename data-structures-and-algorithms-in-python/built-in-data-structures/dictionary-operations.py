# -- coding: utf-8 --
"""

Created on: 22/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Adding/Updating Entries #
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}

phone_book["Godzilla"] = 46394  # New entry
print(phone_book)

phone_book["Godzilla"] = 467582949 # Updating entry
print(phone_book)

# Removing Entries #
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}

del phone_book["Ghostbusters"]
print(phone_book)

# pop() and popitem() #
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678,
              "Woman": 56789}
print(phone_book)

batman = phone_book.pop("Batman")
print(phone_book)
print(batman)

# Remove and return the last pair, as a Tuple.
lastAdded = phone_book.popitem()
lastAdded

# length of a Dictionary #
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(len(phone_book))

# Checking key Existence #
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print("Batman" in phone_book)
print("Godzilla" in phone_book)


# Copying Contents #
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}

second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}

# Add secondphone_book to phone_book
phone_book.update(second_phone_book)
print(phone_book)

# Dictionary Comprehension #
houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n**2: house + "!" for (n, house) in houses.items()}
print(houses)
print(new_houses)



