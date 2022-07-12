# -- coding: utf-8 --
"""

This module highlights the key features of the string data type.

Created on: 12/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# A string is a collection of characters  single, double or triple

print("Harry Potter!")  # Double quotation marks

got = 'Game of Thrones...'  # Single quotation marks
print(got)
print("$")  # Single character

empty = ""
print(empty)  # Just prints an empty line

multiple_lines = '''Triple quotes allows
multi-line string.'''
print(multiple_lines)


# The Length of a String

random_string = "I am Batman"  # 11 characters
print(len(random_string))


# Accessing Characters
batman = "Bruce Wayne"

first = batman[0]  # Accessing the first character
print(first)

space = batman[5]  # Accessing the empty space in the string
print(space)

last = batman[len(batman) - 1]
print(last)
# The following will produce an error since the index is out of bounds
# err = batman[len(batman)]


# Reverse Indexing
batman = "Bruce Wayne"
print(batman[-1])  # Corresponds to batman[10]
print(batman[-5])  # Corresponds to batman[6]


# String Immutability
string = "Immutability"
string[0] = 'O' # Will give error

str1 = "hello"
print(id(str1))

str1 = "bye"
print(id(str1))

# ASCII Versus Unicode#
string = u"This is unicode"
