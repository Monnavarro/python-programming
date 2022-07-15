# -- coding: utf-8 --
"""

Created on: 14/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

# Search #

random_string = "This is a string"

print(random_string.find("is"))
print(random_string.find("is", 9, 13))

# Replace #
a_string = "Welcome to Educative!"
new_string = a_string.replace("Welcome to", "Greetings from")
print(a_string)
print(new_string)

# Changing the Letter Case #
print("UpperCase".upper())
print("LowerCase".lower())

# Joining Strings #
llist = ['a', 'b', 'c']
print(llist)
print('>>'.join(llist)) # joining strings with >>
print('<<'.join(llist)) # joining strings with <<
print(','.join(llist)) # joining strings with comma and space


# Formatting #
string1 = "Learn Python {version} at {cname}".format(version = 3, cname = "Educative")
string2 = "Learn Python {0} at {1}".format(3, "Educative")
string3 = "Learn Python {} at {}".format(3, "Educative")

print(string1)
print(string2)
print(string3)
